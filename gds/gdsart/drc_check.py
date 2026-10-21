#!/usr/bin/env python3
"""Rule checks for the GDS art, values taken from SG13CMOS5L Layout Rules Rev 0.1."""
import sys, klayout.db as kdb
gds = sys.argv[1] if len(sys.argv) > 1 else "chipalooza2_gdsart.gds"
ly = kdb.Layout(); ly.read(gds); top = ly.top_cell()
um = lambda v: int(round(v / ly.dbu))
BOX = kdb.Box(0, 0, um(450), um(25))
R = lambda l, d: kdb.Region(top.begin_shapes_rec(ly.layer(l, d))).merged()

rules = {
 # name     layer      width  space  space_wide(w,run,s)        space_huge(>10um)  min_area  dens(min,max)
 "Metal1":   ((8, 0),   0.16, 0.18, (0.30, 1.0, 0.22), 0.60, 0.09,  (35, 60)),
 "Metal2":   ((10, 0),  0.20, 0.21, (0.39, 1.0, 0.24), 0.60, 0.144, (35, 60)),
 "Metal3":   ((30, 0),  0.20, 0.21, (0.39, 1.0, 0.24), 0.60, 0.144, (35, 60)),
 "Metal4":   ((50, 0),  0.20, 0.21, (0.39, 1.0, 0.24), 0.60, 0.144, (35, 60)),
 "TopMetal1":((126, 0), 1.64, 1.64, None,              None, None,  (25, 70)),
}
fails = 0
def rep(name, rule, n, extra=""):
    global fails
    fails += n > 0
    print(f"  {'PASS' if n == 0 else 'FAIL'}  {rule:<44} {n:>4} {extra}")

# forbidden layers (section 3.2) & layer inventory
forbidden = {(3,0),(11,0),(13,0),(26,0),(32,0),(35,0),(36,0),(53,0),(55,0),(57,0),(58,0),
             (62,0),(66,0),(67,0),(67,22),(71,0),(129,0),(133,0),(134,0),(134,22),(139,0)}
used = {(i.layer, i.datatype) for i in ly.layer_infos() if not top.bbox_per_layer(ly.layer(i)).empty()}
print("Layers used:", sorted(used))
rep("General", "3.2 no forbidden layer (incl. Metal5 67/0)", len(used & forbidden))

for name, (ld, w, s, wide, huge, amin, dens) in rules.items():
    rg = R(*ld)
    print(f"\n{name} {ld}: {rg.count()} polygons")
    rep(name, f"min width {w}", rg.width_check(um(w)).count())
    rep(name, f"min space/notch {s}", rg.space_check(um(s)).count())
    if wide:
        wl, run, ws = wide
        wide_rg = rg - rg.sized(-um(wl/2 + 0.0025)).sized(um(wl/2 + 0.0025)).inverted() if False else rg
        # conservative: apply wide-line spacing to ALL shapes (stricter than DRM)
        rep(name, f"wide-line space {ws} (applied to all shapes)", rg.space_check(um(ws)).count())
    if huge:
        big = rg.sized(-um(5.0)).sized(um(5.0))       # parts wider than 10 um
        rep(name, f"lines >10um wide exist? (then {huge} space)", big.count(),
            "(none -> rule n/a)" if big.count() == 0 else "")
    if amin:
        rep(name, f"min area {amin} um2", rg.with_area(None, int(amin / ly.dbu**2), False).count())
    rep(name, "Slt.c no metal wider than 30 um (no slits)", rg.sized(-um(15.0)).count())
    # grid & angles
    offg = sum(1 for p in rg.each() for pt in p.each_point_hull() if pt.x % 5 or pt.y % 5)
    rep(name, "3.1 all vertices on 5 nm grid", offg)
    rep(name, "3.1 Manhattan / allowed angles", 0 if rg.is_box() or all(p.is_rectilinear() for p in rg.each()) else 1)
    rep(name, "inside 450 x 25 um area", 0 if BOX.contains(rg.bbox().p1) and BOX.contains(rg.bbox().p2) else 1)
    d = 100.0 * rg.area() / BOX.area()
    rep(name, f"density in art area {dens[0]}..{dens[1]} %", 0 if dens[0] <= d <= dens[1] else 1, f"({d:.1f} %)")
    if name != "TopMetal1":
        rep(name, "MFil.h/k coverage 25..75 % (art area)", 0 if 25 <= d <= 75 else 1, f"({d:.1f} %)")

# nofill markers present
for l in (8, 10, 30, 50, 126):
    rg = R(l, 23)
    rep("nofill", f"{l}/23 nofill covers art area", 0 if rg.area() == BOX.area() else 1)
print("\nRESULT:", "CLEAN" if fails == 0 else f"{fails} FAILING CHECKS")
