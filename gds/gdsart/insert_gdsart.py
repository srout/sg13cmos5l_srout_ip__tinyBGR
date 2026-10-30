#!/usr/bin/env python3
"""
insert_gdsart.py - place one or more GDS-art cells into an existing layout (e.g. an analog IP).

Each art GDS is copied into the target layout as its own cell (layers matched by
layer/datatype, dbu converted if different) and instantiated in the target top cell.
Nothing in the IP is flattened or modified; only instances are added.

Usage
  insert_gdsart.py -i ip.gds -o ip_art.gds -p art.gds 120 40
  insert_gdsart.py -i ip.gds -o ip_art.gds -p a.gds 120 40 -p b.gds 300 5 R90 anchor=center
  insert_gdsart.py -i ip.gds -o ip_art.gds -f placements.txt

Placement spec (on the command line after -p, or one per line in a file):
  <gds> <x_um> <y_um> [orient] [key=value ...]

  orient : R0 (default) R90 R180 R270 MX MY MXR90 MYR90
           (MX = mirror about the x-axis, MY = about the y-axis,
            MXR90 = MX then rotate 90, MYR90 = MY then rotate 90)
  keys   : anchor=ll|center|origin   what (x, y) refers to after rotation:
                                     ll     = lower-left of the art boundary (default)
                                     center = centre of the art boundary
                                     origin = the art cell's (0,0)
           name=CELLNAME             cell name for the art in the output (default: art top cell name)
           cell=CELLNAME             which top cell to take from the art GDS (if it has several)

Placement file: '#' starts a comment, blank lines are ignored, relative GDS paths
are resolved against the placement file's directory.

Checks (warnings; --strict turns them into a non-zero exit, no file written):
  * art boundary extends outside the IP boundary
  * existing shapes (IP or earlier art) on any layer the art draws on, inside the art boundary
  * placement off the --grid (it is snapped)
"""
import argparse
import os
import sys

ORIENT = {  # name: (KLayout rotation code 0..3 = 0/90/180/270 deg, mirror about x first)
    "R0": (0, False), "R90": (1, False), "R180": (2, False), "R270": (3, False),
    "MX": (0, True), "MY": (2, True), "MXR90": (1, True), "MYR90": (3, True),
}
ANCHORS = ("ll", "center", "origin")


class Placement:
    def __init__(self, gds, x, y, orient="R0", anchor=None, name=None, cell=None, src=""):
        self.gds, self.x, self.y = gds, x, y
        self.orient, self.anchor, self.name, self.cell, self.src = orient, anchor, name, cell, src


def parse_tokens(tokens, base_dir, src):
    if len(tokens) < 3:
        raise ValueError(f"{src}: need at least '<gds> <x> <y>', got {' '.join(tokens)!r}")
    gds = tokens[0]
    if not os.path.isabs(gds):
        gds = os.path.normpath(os.path.join(base_dir, gds))
    try:
        x, y = float(tokens[1]), float(tokens[2])
    except ValueError:
        raise ValueError(f"{src}: x/y must be numbers (um), got {tokens[1]!r} {tokens[2]!r}")
    p = Placement(gds, x, y, src=src)
    for t in tokens[3:]:
        if "=" in t:
            k, v = t.split("=", 1)
            k = k.lower()
            if k == "anchor":
                if v.lower() not in ANCHORS:
                    raise ValueError(f"{src}: anchor must be one of {ANCHORS}, got {v!r}")
                p.anchor = v.lower()
            elif k == "name":
                p.name = v
            elif k == "cell":
                p.cell = v
            else:
                raise ValueError(f"{src}: unknown key {k!r} (use anchor=, name=, cell=)")
        elif t.upper() in ORIENT:
            p.orient = t.upper()
        else:
            raise ValueError(f"{src}: unknown token {t!r} (orient is one of {', '.join(ORIENT)})")
    return p


def read_placement_file(path):
    out, base = [], os.path.dirname(os.path.abspath(path))
    with open(path) as fh:
        for n, line in enumerate(fh, 1):
            toks = line.split("#", 1)[0].split()
            if toks:
                out.append(parse_tokens(toks, base, f"{path}:{n}"))
    return out


def parse_layer(spec):
    try:
        l, d = spec.split("/")
        return int(l), int(d)
    except ValueError:
        raise argparse.ArgumentTypeError(f"layer must look like 189/0, got {spec!r}")


# ---------------------------------------------------------------- klayout part
def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Insert GDS-art cells into an existing GDS at given locations.",
        epilog="Placement spec: <gds> <x_um> <y_um> [orient] [anchor=ll|center|origin] [name=..] [cell=..]")
    ap.add_argument("-i", "--input", required=True, help="target layout (GDS/OASIS)")
    ap.add_argument("-o", "--output", required=True, help="output layout (format from extension)")
    ap.add_argument("-p", "--place", action="append", nargs="+", default=[], metavar="SPEC",
                    help="one placement; repeat -p for more")
    ap.add_argument("-f", "--file", action="append", default=[], help="placement file; may repeat")
    ap.add_argument("-t", "--top", help="target top cell (needed if the input has several top cells)")
    ap.add_argument("--anchor", default="ll", choices=ANCHORS, help="default anchor (default: ll)")
    ap.add_argument("--boundary", type=parse_layer, default=(189, 0),
                    help="boundary layer for art/IP extent (default 189/0 = IHP prBoundary)")
    ap.add_argument("--grid", type=float, default=0.005, help="placement grid in um (default 0.005)")
    ap.add_argument("--strict", action="store_true", help="fail (write nothing) on any warning")
    a = ap.parse_args(argv)

    try:
        places = [parse_tokens(t, os.getcwd(), f"-p #{i+1}") for i, t in enumerate(a.place)]
        for f in a.file:
            places += read_placement_file(f)
    except (ValueError, OSError) as e:
        ap.error(str(e))
    if not places:
        ap.error("no placements given (use -p and/or -f)")
    if os.path.abspath(a.input) == os.path.abspath(a.output):
        ap.error("output must differ from input")
    for p in places:
        if not os.path.isfile(p.gds):
            ap.error(f"{p.src}: art file not found: {p.gds}")

    import klayout.db as kdb

    def pick_top(layout, name, what):
        if name:
            c = layout.cell(name)
            if c is None:
                sys.exit(f"error: cell {name!r} not found in {what}")
            return c
        tops = layout.top_cells()
        if len(tops) != 1:
            sys.exit(f"error: {what} has {len(tops)} top cells "
                     f"({', '.join(c.name for c in tops)}); choose one")
        return tops[0]

    def extent(layout, cell):
        """boundary-layer bbox if present, else bbox of all polygons (texts ignored), in um"""
        li = layout.find_layer(*a.boundary)
        if li is not None:
            r = kdb.Region(cell.begin_shapes_rec(li))
            if not r.is_empty():
                return r.bbox().to_dtype(layout.dbu), True
        box = kdb.Box()
        for li in layout.layer_indexes():
            box += kdb.Region(cell.begin_shapes_rec(li)).bbox()
        return box.to_dtype(layout.dbu), False

    def unique_name(layout, base):
        name, i = base, 1
        while layout.has_cell(name):
            name, i = f"{base}_{i}", i + 1
        return name

    ly = kdb.Layout()
    ly.read(a.input)
    top = pick_top(ly, a.top, a.input)
    dbu = ly.dbu
    ip_box, ip_has_bnd = extent(ly, top)
    print(f"target : {a.input}  top={top.name}  dbu={dbu}  "
          f"extent={'prBoundary' if ip_has_bnd else 'bbox'} {ip_box}")

    cache, warnings, report = {}, [], []
    for p in places:
        key = (p.gds, p.cell, p.name)
        if key not in cache:
            src = kdb.Layout()
            src.read(p.gds)
            sc = pick_top(src, p.cell, p.gds)
            if abs(src.dbu - dbu) > 1e-12:
                warnings.append(f"{p.src}: art dbu {src.dbu} != target dbu {dbu} (shapes rescaled)")
            box, has_bnd = extent(src, sc)
            if not has_bnd:
                print(f"note   : {p.gds} has no {a.boundary[0]}/{a.boundary[1]} boundary; "
                      f"using polygon bbox")
            layers = []
            for li in src.layer_indexes():
                info = src.get_info(li)
                if (info.layer, info.datatype) == a.boundary:
                    continue
                if not kdb.Region(sc.begin_shapes_rec(li)).is_empty():
                    layers.append(kdb.LayerInfo(info.layer, info.datatype))
            new = ly.create_cell(unique_name(ly, p.name or sc.name))
            new.copy_tree(sc)
            cache[key] = (new.cell_index(), new.name, box, layers)
        ci, cname, box, layers = cache[key]

        rot, mir = ORIENT[p.orient]
        t0 = kdb.DTrans(rot, mir, 0.0, 0.0)
        tb = t0 * box
        anchor = p.anchor or a.anchor
        ref = {"ll": tb.p1, "center": tb.center(), "origin": kdb.DPoint(0, 0)}[anchor]
        dx, dy = p.x - ref.x, p.y - ref.y
        sx, sy = round(dx / a.grid) * a.grid, round(dy / a.grid) * a.grid
        if abs(sx - dx) > 1e-9 or abs(sy - dy) > 1e-9:
            warnings.append(f"{p.src}: offset ({dx:.4f}, {dy:.4f}) snapped to {a.grid} um grid "
                            f"-> ({sx:.4f}, {sy:.4f})")
        t = kdb.DTrans(rot, mir, sx, sy)
        pb = t * box

        if not pb.inside(ip_box):
            warnings.append(f"{p.src}: art box {pb} extends outside IP extent {ip_box}")

        ibox = pb.to_itype(dbu)
        clash = []
        for info in layers:
            lt = ly.find_layer(info)
            if lt is None:
                continue
            it = top.begin_shapes_rec(lt)
            it.region = ibox
            ov = kdb.Region(it) & kdb.Region(ibox)
            if not ov.is_empty():
                clash.append(f"{info.layer}/{info.datatype}: {ov.area() * dbu * dbu:.2f} um2")
        if clash:
            warnings.append(f"{p.src}: existing shapes under art box {pb}: " + ", ".join(clash))

        top.insert(kdb.DCellInstArray(ci, t))
        report.append(f"  {cname:<28} {p.orient:<6} anchor={anchor:<6} "
                      f"box=({pb.left:.3f},{pb.bottom:.3f})..({pb.right:.3f},{pb.top:.3f})")

    print("placed :")
    print("\n".join(report))
    for w in warnings:
        print("WARNING:", w)
    if warnings and a.strict:
        sys.exit(f"{len(warnings)} warning(s) with --strict: nothing written")
    ly.write(a.output)
    print(f"wrote  : {a.output}  ({len(places)} instance(s), {len(cache)} art cell(s))")


if __name__ == "__main__":
    main()
