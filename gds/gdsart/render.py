import klayout.db as kdb, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection
ly=kdb.Layout(); ly.read("chipalooza2_gdsart.gds"); top=ly.top_cell()
def polys(l,d):
    rg=kdb.Region(top.begin_shapes_rec(ly.layer(l,d))).merged()
    out=[]
    for p in rg.each():
        for t in kdb.Region(p).decompose_trapezoids_to_region().each():
            out.append([(q.x/1000,q.y/1000) for q in t.each_point_hull()])
    return out
LAY=[("Metal1 (8/0) - LED matrix",8,"#2b6cff"),("Metal2 (10/0) - stencil/negative",10,"#c040ff"),
     ("Metal3 (30/0) - deep shadow + tiles",30,"#20b070"),("Metal4 (50/0) - shadow + tiles",50,"#ff9020"),
     ("TopMetal1 (126/0) - text + frame",126,"#e8c547")]
P={l:polys(l,0) for _,l,_ in LAY}
def draw(ax,layers,xl=(0,450),alpha=None):
    ax.set_facecolor("#0c0f14")
    for name,l,c in layers:
        ax.add_collection(PolyCollection(P[l],facecolors=c,edgecolors="none",alpha=alpha or 1))
    ax.plot([0,450,450,0,0],[0,0,25,25,0],color="#888",lw=0.6,ls="--")
    ax.set_xlim(*xl); ax.set_ylim(-0.5,25.5); ax.set_aspect("equal"); ax.set_xticks([]); ax.set_yticks([])
# full stack
fig,ax=plt.subplots(figsize=(36,2.4),dpi=150); fig.patch.set_facecolor("#0c0f14")
draw(ax,LAY,alpha=0.75); plt.subplots_adjust(0.005,0.02,0.995,0.98); fig.savefig("preview_stack_full.png",facecolor=fig.get_facecolor()); plt.close()
# per layer, full width
fig,axs=plt.subplots(5,1,figsize=(36,12),dpi=110); fig.patch.set_facecolor("#0c0f14")
for ax,L in zip(axs,LAY):
    draw(ax,[L]); ax.set_title(L[0],color="w",fontsize=16,loc="left")
plt.tight_layout(); fig.savefig("preview_layers.png",facecolor=fig.get_facecolor()); plt.close()
# zoom crop of stack
fig,axs=plt.subplots(2,1,figsize=(16,5.5),dpi=150); fig.patch.set_facecolor("#0c0f14")
draw(axs[0],LAY,xl=(0,120),alpha=0.75); axs[0].set_title("Stacked view, x = 0..120 um",color="w",loc="left")
draw(axs[1],LAY,xl=(330,450),alpha=0.75); axs[1].set_title("Stacked view, x = 330..450 um",color="w",loc="left")
plt.tight_layout(); fig.savefig("preview_stack_zoom.png",facecolor=fig.get_facecolor()); plt.close()
