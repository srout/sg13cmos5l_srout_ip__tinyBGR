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
"""
import klayout.db as kdb

UM = 1000                       # dbu = 1 nm
G = 5                           # 5 nm grid
def u(v):                       # um -> dbu snapped to 5 nm grid
    return int(round(v * UM / G)) * G

TEXT = "(c) 2026  CHIPALOOZA#2   IHP-SG13CMOS5L  TinyBGR"
W, H = 450.0, 25.0

L = {  # name: (layer, datatype)
    "M1": (8, 0), "M2": (10, 0), "M3": (30, 0), "M4": (50, 0), "TM1": (126, 0),
    "M1_nofill": (8, 23), "M2_nofill": (10, 23), "M3_nofill": (30, 23),
    "M4_nofill": (50, 23), "TM1_nofill": (126, 23),
    "prBoundary": (189, 0), "TEXT": (63, 0),
}

# ---------------------------------------------------------------- font
# 7-row, square, strictly 4-connected pixel font (no corner-only contacts,
# so every merged polygon is DRC-clean at any pixel pitch >= min space).
F = {
"(": [".XX","XX.","X..","X..","X..","XX.",".XX"],
")": ["XX.",".XX","..X","..X","..X",".XX","XX."],
"c": ["....","....","XXXX","X...","X...","X...","XXXX"],
"0": ["XXXXX","X...X","X...X","X.X.X","X...X","X...X","XXXXX"],
"1": ["XX.",".X.",".X.",".X.",".X.",".X.","XXX"],
"2": ["XXXXX","....X","....X","XXXXX","X....","X....","XXXXX"],
"3": ["XXXXX","....X","....X",".XXXX","....X","....X","XXXXX"],
"5": ["XXXXX","X....","XXXXX","....X","....X","....X","XXXXX"],
"6": ["XXXXX","X....","X....","XXXXX","X...X","X...X","XXXXX"],
"A": ["XXXXX","X...X","X...X","XXXXX","X...X","X...X","X...X"],
"B": ["XXXX.","X..X.","X..X.","XXXXX","X...X","X...X","XXXXX"],
"C": ["XXXXX","X....","X....","X....","X....","X....","XXXXX"],
"G": ["XXXXX","X....","X....","X..XX","X...X","X...X","XXXXX"],
"H": ["X...X","X...X","X...X","XXXXX","X...X","X...X","X...X"],
"I": ["XXX",".X.",".X.",".X.",".X.",".X.","XXX"],
"L": ["X....","X....","X....","X....","X....","X....","XXXXX"],
"M": ["XXXXX","X.X.X","X.X.X","X.X.X","X...X","X...X","X...X"],
"O": ["XXXXX","X...X","X...X","X...X","X...X","X...X","XXXXX"],
"P": ["XXXXX","X...X","X...X","XXXXX","X....","X....","X...."],
"R": ["XXXXX","X...X","X...X","XXXXX","X..X.","X..XX","X...X"],
"S": ["XXXXX","X....","X....","XXXXX","....X","....X","XXXXX"],
"T": ["XXXXX","..X..","..X..","..X..","..X..","..X..","..X.."],
"Z": ["XXXXX","....X","...XX","..XX.",".XX..","XX...","XXXXX"],
"#": [".X.X.",".X.X.","XXXXX",".X.X.","XXXXX",".X.X.",".X.X."],
"-": ["...","...","...","XXX","...","...","..."],
"i": ["X",".","X","X","X","X","X"],
"n": [".....",".....","XXXXX","X...X","X...X","X...X","X...X"],
"y": [".....",".....","X...X","X...X","XXXXX","....X","XXXXX"],
}
SPACE_COLS = 3
ROWS = 7

def check_font():
    for ch, g in F.items():
        w = len(g[0]); assert all(len(r) == w for r in g), ch
        on = lambda r, c: 0 <= r < ROWS and 0 <= c < w and g[r][c] == "X"
        for r in range(ROWS):
            for c in range(w):
                for dr, dc in ((1, 1), (1, -1)):
                    if on(r, c) and on(r+dr, c+dc) and not on(r+dr, c) and not on(r, c+dc):
                        raise SystemExit(f"diagonal-only contact in glyph {ch!r}")

def bitmap(text):
    """return list of lit (col,row) cells, total columns"""
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

# ---------------------------------------------------------------- geometry
check_font()
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

# ---- Metal1 : "LED matrix"  big dot = lit pixel, small dot = unlit pixel
BIG_X, BIG_Y = 0.20, 0.20       # inset per side -> 0.40 um gaps
SMALL_X, SMALL_Y = 1.00, 1.60   # unlit dot size (um)
m1 = kdb.Region()
for c, r in grid:
    if (c, r) in lit:
        m1.insert(cell_box(c, r, BIG_X, BIG_Y))
    else:
        b = cell_box(c, r)
        cx, cy = b.center().x, b.center().y; hx, hy = u(SMALL_X/2), u(SMALL_Y/2)
        m1.insert(kdb.Box(cx-hx, cy-hy, cx+hx, cy+hy))
M1 = (m1 & lo_area).merged()

# ---- Metal2 : negative / stencil  (tiles only where text is NOT)
m2 = kdb.Region()
for c, r in grid:
    if (c, r) not in lit:
        m2.insert(cell_box(c, r, 0.21, 0.21))
M2 = (m2 & lo_area).merged()

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
M3 = shadow_layer(2*px/3, -2*py/3, 1.00, 2.40, 1.60, 3.00, 0.80)

# ---------------------------------------------------------------- write
ly = kdb.Layout(); ly.dbu = 0.001
top = ly.create_cell("CHIPALOOZA2_GDSART")
li = {k: ly.layer(*v) for k, v in L.items()}
for name, rg in (("M1", M1), ("M2", M2), ("M3", M3), ("M4", M4), ("TM1", TM1)):
    top.shapes(li[name]).insert(rg)
for n in ("M1_nofill", "M2_nofill", "M3_nofill", "M4_nofill", "TM1_nofill", "prBoundary"):
    top.shapes(li[n]).insert(BOX)
top.shapes(li["TEXT"]).insert(kdb.Text("CHIPALOOZA2_GDSART", kdb.Trans(u(1), u(H+1))))
#ly.write("/home/user/workspace/gdsart/chipalooza2_gdsart.gds")
ly.write("chipalooza2_gdsart.gds")

import json
json.dump({"px": px, "py": py, "ncols": ncols, "x0": x0/UM, "y0": y0/UM,
           "text_w": tw, "text_h": th}, open("params.json", "w"), indent=1)
print("pitch", px, py, "cols", ncols, "text", round(tw, 3), "x", round(th, 3))
