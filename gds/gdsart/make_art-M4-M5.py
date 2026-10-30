#!/usr/bin/env python3
"""
GDS text artwork for IHP SG13CMOS5L (Metal1..Metal4 + TopMetal1)
Text : "(c) 2026  CHIPALOOZA#2   IHP-SG13CMOS5L  TinyBGR"
Area : 450 um x 25 um   (cell origin = lower-left corner)

Rules used (SG13CMOS5L Layout Rules Rev 0.1):
  Grid 3.1      : 5 nm drawing grid, Manhattan only
  Forbidden 3.2 : Metal5 (67/0) is forbidden  -> 5th metal is TopMetal1 (126/0)
  M1.a/b/d/e    : 0.16 / 0.18 / 0.09um2 / 0.22 (w>0.3, run>1)
  Mn.a/b/d/e/f  : 0.20 / 0.21 / 0.144um2 / 0.24 (w>0.39) / 0.60 (w>10)
  M1.j/k Mn.j/k : 35..60 % density
  MFil.h/k      : 25..75 % coverage
  TM1.a/b/c/d   : 1.64 / 1.64 / 25..70 % density
  Slt.c         : metal wider than 30 um needs slits (avoided)

Run with --preview to print the text as ASCII art and exit (no klayout needed).
"""
import sys

UM = 1000                       # dbu = 1 nm
G = 5                           # 5 nm grid
def u(v):                       # um -> dbu snapped to 5 nm grid
    return int(round(v * UM / G)) * G

#TEXT = "(c) 2026  CHIPALOOZA#2   IHP-SG13CMOS5L  TinyBGR"
#W, H = 450.0, 25.0
#TEXT = " 0 i 0 "
#W, H = 250.0, 90.0
#TEXT = "#CNIC #SILICON #ODISHA"
#W, H = 230.0, 25.0
TEXT = "|------- 250um -------|"
W, H = 250.0, 25.0


L = {  # name: (layer, datatype)
    "M4": (50, 0), "TM1": (126, 0),
    "M4_nofill": (50, 23), "TM1_nofill": (126, 23),
    "prBoundary": (189, 0), "TEXT": (63, 0),
}

# ---------------------------------------------------------------- font
# 7-row, square, strictly 4-connected pixel font (no corner-only contacts,
# so every merged polygon is DRC-clean at any pixel pitch >= min space).
# Row 0 = top. Lowercase x-height = rows 2..6; ascenders use rows 0..6;
# descender letters (g j p q y) are folded into rows 2..6.
# Covers all printable ASCII 0x21..0x7E; space is handled by SPACE_COLS.
F = {
# ---- digits
"0": ["XXXXX","X...X","X...X","X.X.X","X...X","X...X","XXXXX"],
"1": ["XX.",".X.",".X.",".X.",".X.",".X.","XXX"],
"2": ["XXXXX","....X","....X","XXXXX","X....","X....","XXXXX"],
"3": ["XXXXX","....X","....X",".XXXX","....X","....X","XXXXX"],
"4": ["X...X","X...X","X...X","XXXXX","....X","....X","....X"],
"5": ["XXXXX","X....","XXXXX","....X","....X","....X","XXXXX"],
"6": ["XXXXX","X....","X....","XXXXX","X...X","X...X","XXXXX"],
"7": ["XXXXX","....X","....X","...XX","..XX.","..X..","..X.."],
"8": ["XXXXX","X...X","X...X","XXXXX","X...X","X...X","XXXXX"],
"9": ["XXXXX","X...X","X...X","XXXXX","....X","....X","XXXXX"],
# ---- uppercase
"A": ["XXXXX","X...X","X...X","XXXXX","X...X","X...X","X...X"],
"B": ["XXXX.","X..X.","X..X.","XXXXX","X...X","X...X","XXXXX"],
"C": ["XXXXX","X....","X....","X....","X....","X....","XXXXX"],
"D": ["XXXX.","X..XX","X...X","X...X","X...X","X..XX","XXXX."],
"E": ["XXXXX","X....","X....","XXXX.","X....","X....","XXXXX"],
"F": ["XXXXX","X....","X....","XXXX.","X....","X....","X...."],
"G": ["XXXXX","X....","X....","X..XX","X...X","X...X","XXXXX"],
"H": ["X...X","X...X","X...X","XXXXX","X...X","X...X","X...X"],
"I": ["XXX",".X.",".X.",".X.",".X.",".X.","XXX"],
"J": ["....X","....X","....X","....X","X...X","X...X","XXXXX"],
"K": ["X...X","X..XX","X.XX.","XXX..","X.XX.","X..XX","X...X"],
"L": ["X....","X....","X....","X....","X....","X....","XXXXX"],
"M": ["XXXXX","X.X.X","X.X.X","X.X.X","X...X","X...X","X...X"],
"N": ["X...X","XX..X","XXX.X","X.XXX","X..XX","X...X","X...X"],
"O": ["XXXXX","X...X","X...X","X...X","X...X","X...X","XXXXX"],
"P": ["XXXXX","X...X","X...X","XXXXX","X....","X....","X...."],
"Q": ["XXXXX","X...X","X...X","X...X","X.X.X","X.XXX","XXXXX"],
"R": ["XXXXX","X...X","X...X","XXXXX","X..X.","X..XX","X...X"],
"S": ["XXXXX","X....","X....","XXXXX","....X","....X","XXXXX"],
"T": ["XXXXX","..X..","..X..","..X..","..X..","..X..","..X.."],
"U": ["X...X","X...X","X...X","X...X","X...X","X...X","XXXXX"],
"V": ["X...X","X...X","X...X","XX.XX",".X.X.",".XXX.","..X.."],
"W": ["X...X","X...X","X...X","X.X.X","X.X.X","X.X.X","XXXXX"],
"X": ["X...X","XX.XX",".XXX.","..X..",".XXX.","XX.XX","X...X"],
"Y": ["X...X","X...X","XX.XX",".XXX.","..X..","..X..","..X.."],
"Z": ["XXXXX","....X","...XX","..XX.",".XX..","XX...","XXXXX"],
# ---- lowercase
"a": [".....",".....","XXXXX","....X","XXXXX","X...X","XXXXX"],
"b": ["X....","X....","XXXXX","X...X","X...X","X...X","XXXXX"],
"c": ["....","....","XXXX","X...","X...","X...","XXXX"],
"d": ["....X","....X","XXXXX","X...X","X...X","X...X","XXXXX"],
"e": [".....",".....","XXXXX","X...X","XXXXX","X....","XXXXX"],
"f": [".XXX",".X..","XXXX",".X..",".X..",".X..",".X.."],
"g": [".....",".....","XXXXX","X...X","XXXXX","....X","XXXXX"],
"h": ["X....","X....","XXXXX","X...X","X...X","X...X","X...X"],
"i": ["X",".","X","X","X","X","X"],
"j": ["..X","...","..X","..X","..X","..X","XXX"],
"k": ["X...","X...","X..X","X.XX","XXX.","X.XX","X..X"],
"l": ["XX.",".X.",".X.",".X.",".X.",".X.",".XX"],
"m": [".....",".....","XXXXX","X.X.X","X.X.X","X.X.X","X.X.X"],
"n": [".....",".....","XXXXX","X...X","X...X","X...X","X...X"],
"o": [".....",".....","XXXXX","X...X","X...X","X...X","XXXXX"],
"p": [".....",".....","XXXXX","X...X","XXXXX","X....","X...."],
"q": [".....",".....","XXXXX","X...X","XXXXX","....X","....X"],
"r": ["....","....","XXXX","X...","X...","X...","X..."],
"s": [".....",".....","XXXXX","X....","XXXXX","....X","XXXXX"],
"t": [".X..",".X..","XXXX",".X..",".X..",".X..",".XXX"],
"u": [".....",".....","X...X","X...X","X...X","X...X","XXXXX"],
"v": [".....",".....","X...X","X...X","XX.XX",".XXX.","..X.."],
"w": [".....",".....","X...X","X.X.X","X.X.X","X.X.X","XXXXX"],
"x": [".....",".....","XX.XX",".XXX.","..X..",".XXX.","XX.XX"],
"y": [".....",".....","X...X","X...X","XXXXX","....X","XXXXX"],
"z": [".....",".....","XXXXX","...XX","..XX.",".XX..","XXXXX"],
# ---- punctuation / symbols
"!": ["X","X","X","X","X",".","X"],
'"': ["X.X","X.X","...","...","...","...","..."],
"#": [".X.X.",".X.X.","XXXXX",".X.X.","XXXXX",".X.X.",".X.X."],
"$": ["..X..","XXXXX","X.X..","XXXXX","..X.X","XXXXX","..X.."],
"%": ["X..XX","...X.","..XX.","..X..",".XX..",".X...","XX..X"],
"&": ["XXX..","X.X..","XXX..","XXX.X","X.XXX","X..X.","XXXXX"],
"'": ["X","X",".",".",".",".","."],
"(": [".XX","XX.","X..","X..","X..","XX.",".XX"],
")": ["XX.",".XX","..X","..X","..X",".XX","XX."],
"*": [".....","X.X.X","XXXXX",".XXX.","XXXXX","X.X.X","....."],
"+": [".....","..X..","..X..","XXXXX","..X..","..X..","....."],
",": ["..","..","..","..",".X",".X","XX"],
"-": ["...","...","...","XXX","...","...","..."],
".": [".",".",".",".",".",".","X"],
"/": ["....X","...XX","...X.","..XX.",".XX..",".X...","XX..."],
":": [".",".","X",".",".",".","X"],
";": ["..","..",".X","..",".X",".X","XX"],
"<": ["...X","..XX",".XX.","XX..",".XX.","..XX","...X"],
"=": ["....","....","XXXX","....","XXXX","....","...."],
">": ["X...","XX..",".XX.","..XX",".XX.","XX..","X..."],
"?": ["XXXXX","....X","....X","..XXX","..X..",".....","..X.."],
"@": ["XXXXX","X...X","X.XXX","X.X.X","X.XXX","X....","XXXXX"],
"[": ["XX","X.","X.","X.","X.","X.","XX"],
"\\": ["X....","XX...",".X...",".XX..","..XX.","...X.","...XX"],
"]": ["XX",".X",".X",".X",".X",".X","XX"],
"^": ["..X..",".XXX.","XX.XX","X...X",".....",".....","....."],
"_": [".....",".....",".....",".....",".....",".....","XXXXX"],
"`": ["X.","XX","..","..","..","..",".."],
"{": [".XX",".X.",".X.","XX.",".X.",".X.",".XX"],
"|": ["X","X","X","X","X","X","X"],
"}": ["XX.",".X.",".X.",".XX",".X.",".X.","XX."],
"~": [".....",".....","XXX.X","X.XXX",".....",".....","....."],
}
SPACE_COLS = 3
ROWS = 7

def check_font():
    for ch, g in F.items():
        assert len(g) == ROWS, f"glyph {ch!r} has {len(g)} rows"
        w = len(g[0]); assert all(len(r) == w for r in g), ch
        on = lambda r, c: 0 <= r < ROWS and 0 <= c < w and g[r][c] == "X"
        for r in range(ROWS):
            for c in range(w):
                for dr, dc in ((1, 1), (1, -1)):
                    if on(r, c) and on(r+dr, c+dc) and not on(r+dr, c) and not on(r, c+dc):
                        raise SystemExit(f"diagonal-only contact in glyph {ch!r}")

def bitmap(text):
    """return list of lit (col,row) cells, total columns"""
    bad = sorted({ch for ch in text if ch != " " and ch not in F})
    if bad:
        raise SystemExit(f"no glyph for: {''.join(bad)!r}")
    cells, x = [], 0
    for ch in text:
        if ch == " ":
            x += SPACE_COLS; continue
        g = F[ch]
        for r in range(ROWS):
            for c, v in enumerate(g[r]):
                if v == "X":
                    cells.append((x + c, ROWS - 1 - r))   # row 0 = bottom
        x += len(g[0]) + 1
    return cells, x - 1

def preview(text):
    cells, ncols = bitmap(text)
    lit = set(cells)
    for r in range(ROWS - 1, -1, -1):
        print("".join("#" if (c, r) in lit else "." for c in range(ncols)))

# ---------------------------------------------------------------- geometry
check_font()
if "--preview" in sys.argv:
    preview(TEXT); sys.exit(0)

import klayout.db as kdb
cells, ncols = bitmap(TEXT)

EDGE_LO = 0.30     # keep Metal1-4 >= 0.30 um inside the cell edge (abutment safety)
EDGE_TM = 0.85     # keep TopMetal1 >= 0.85 um inside the cell edge (half of 1.64 + margin)
FRAME = 1.80       # TopMetal1 frame width  (>= TM1.a 1.64)
GAP_TM = 1.70      # frame-to-text space    (>= TM1.b 1.64)

inner_x0 = EDGE_TM + FRAME + GAP_TM
inner_w = W - 2 * inner_x0
inner_h = H - 2 * inner_x0
px = int(inner_w / ncols / 0.01) * 0.01           # column pitch
py = int(inner_h / ROWS / 0.01) * 0.01            # row pitch
assert px >= 1.64 and py >= 1.64, (px, py)
tw, th = ncols * px, ROWS * py
x0 = u((W - tw) / 2); y0 = u((H - th) / 2)
PX, PY = u(px), u(py)

def cell_box(c, r, inset_x=0.0, inset_y=0.0):
    return kdb.Box(x0 + c*PX + u(inset_x), y0 + r*PY + u(inset_y),
                   x0 + (c+1)*PX - u(inset_x), y0 + (r+1)*PY - u(inset_y))

lit = set(cells)
text_rg = kdb.Region([cell_box(c, r) for c, r in cells]); text_rg.merge()

BOX = kdb.Box(0, 0, u(W), u(H))
lo_area = kdb.Region(BOX.enlarged(-u(EDGE_LO), -u(EDGE_LO)))

# ---- TopMetal1 : solid text + frame
tm_outer = kdb.Box(u(EDGE_TM), u(EDGE_TM), u(W-EDGE_TM), u(H-EDGE_TM))
frame = kdb.Region(tm_outer) - kdb.Region(tm_outer.enlarged(-u(FRAME), -u(FRAME)))
TM1 = (text_rg + frame).merged()

# full-box cell grid indices (grid extended past the text block)
c_lo = -((x0 - u(EDGE_LO)) // PX); c_hi = (u(W - EDGE_LO) - x0) // PX
r_lo = -((y0 - u(EDGE_LO)) // PY); r_hi = (u(H - EDGE_LO) - y0) // PY
grid = [(c, r) for c in range(c_lo, c_hi) for r in range(r_lo, r_hi)]

# ---- Metal4 / Metal3 : 3-D extrusion shadows + keep-out-cut background tiles
def shadow_layer(dx, dy, tile_w, tile_h, pitch_x, pitch_y, stagger, keep=0.60):
    sh = text_rg.moved(u(dx), u(dy))
    ko = sh.sized(u(keep))
    tiles = kdb.Region()
    yy, row = u(EDGE_LO), 0
    while yy + u(tile_h) <= u(H - EDGE_LO):
        xx = u(EDGE_LO) + (u(stagger) if row % 2 else 0)
        while xx + u(tile_w) <= u(W - EDGE_LO):
            tiles.insert(kdb.Box(xx, yy, xx + u(tile_w), yy + u(tile_h)))
            xx += u(pitch_x)
        yy += u(pitch_y); row += 1
    tiles = tiles.select_not_interacting(ko)     # whole tiles only, no slivers
    return (sh + tiles).merged() & lo_area

M4 = shadow_layer(px/3, -py/3, 2.40, 1.00, 3.00, 1.60, 1.50)

# ---------------------------------------------------------------- write
ly = kdb.Layout(); ly.dbu = 0.001
top = ly.create_cell("CHIPALOOZA2_GDSART")
li = {k: ly.layer(*v) for k, v in L.items()}
for name, rg in (("M4", M4), ("TM1", TM1)):
    top.shapes(li[name]).insert(rg)
for n in ("M4_nofill", "TM1_nofill", "prBoundary"):
    top.shapes(li[n]).insert(BOX)
top.shapes(li["TEXT"]).insert(kdb.Text("CHIPALOOZA2_GDSART", kdb.Trans(u(1), u(H+1))))
#ly.write("/home/user/workspace/gdsart/chipalooza2_gdsart.gds")
ly.write("gdsart.gds")

import json
json.dump({"px": px, "py": py, "ncols": ncols, "x0": x0/UM, "y0": y0/UM,
           "text_w": tw, "text_h": th}, open("params.json", "w"), indent=1)
print("pitch", px, py, "cols", ncols, "text", round(tw, 3), "x", round(th, 3))
