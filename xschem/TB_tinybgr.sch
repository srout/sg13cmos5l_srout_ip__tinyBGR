v {xschem version=3.4.8RC file_version=1.3}
G {}
K {}
V {}
S {}
F {}
E {}
N -300 -40 -300 -30 {lab=ADD5V}
N -300 -40 -140 -40 {lab=ADD5V}
N -300 40 -300 70 {lab=0}
N -300 40 -140 40 {lab=0}
N -300 30 -300 40 {lab=0}
N 160 -20 380 -20 {lab=VREF}
N 380 -20 380 40 {lab=VREF}
N 160 0 310 0 {lab=IOUT1}
N 310 0 310 40 {lab=IOUT1}
N 380 100 380 120 {lab=0}
N 310 120 380 120 {lab=0}
N 310 100 310 120 {lab=0}
N 290 120 310 120 {lab=0}
N 290 120 290 130 {lab=0}
C {vsource.sym} -300 0 0 0 {name=Vsup value="PAR_VDD5" savecurrent=false}
C {gnd.sym} -300 70 0 0 {name=l1 lab=0}
C {capa.sym} 380 70 0 0 {name=C3
m=1
value=10f
footprint=1206
device="ceramic capacitor"}
C {lab_wire.sym} -200 -40 0 0 {name=p1 sig_type=std_logic lab=ADD5V}
C {gnd.sym} 290 130 0 0 {name=l2 lab=0}
C {lab_wire.sym} 260 -20 0 0 {name=p2 sig_type=std_logic lab=VREF}
C {lab_wire.sym} 260 0 0 0 {name=p3 sig_type=std_logic lab=IOUT1}
C {devices/code_shown.sym} -330 200 0 0 {name=spcom only_toplevel=false value=".option savecurrents
.PARAM PAR_VDD5=3.3
.PARAM PAR_VDDRISE=100e-6
.PARAM PAR_POFF=0
.PARAM PAR_NOFF=0

.control
run
save all

op
write tb_bgr_op.raw
** To find model parameters type "display" in ngspice prompt
print @n.xbgrtop.xmn1.nsg13_hv_nmos[ids] @n.xbgrtop.xmn1.nsg13_hv_nmos[gm]
print @n.xbgrtop.xmp1.nsg13_hv_pmos[ids] @n.xbgrtop.xmp1.nsg13_hv_pmos[gm]
LET gmidmn1=@n.xbgrtop.xmn1.nsg13_hv_nmos[gm]/@n.xbgrtop.xmn1.nsg13_hv_nmos[ids]
LET gmidmp1=@n.xbgrtop.xmp1.nsg13_hv_pmos[gm]/@n.xbgrtop.xmp1.nsg13_hv_pmos[ids]
print gmidmn1 gmidmp1
print @q.xbgrtop.xq2.qpnpmpa[ie] @q.xbgrtop.xq1.qpnpmpa[ie]
* dc Vref 3.3 1.5 -0.1
DC TEMP -40 125 1
write dc.raw
PLOT V(VREF) 
**PLOT I(VIOUT1)
** PLOT @n.xbgrtop.xmnsu1.nsg13_hv_nmos[ids] 
**PLOT @n.xbgrtop.xmnsu2.nsg13_hv_nmos[ids] 
**PLOT V(xbgrtop.vgsu1)
** Calculating tempco
MEAS DC vrefMAX_m40to125 MAX V(VREF) FROM=-40 TO=125
MEAS DC vrefMIN_m40to125 MIN V(VREF) FROM=-40 TO=125
MEAS DC vrefMAX_m30to85 MAX V(VREF) FROM=-30 TO=85
MEAS DC vrefMIN_m30to85 MIN V(VREF) FROM=-30 TO=85
MEAS DC Iout25 FIND I(VIOUT1) At=25

LET tempco_m40_125_ppmC=1e6*(vrefMAX_m40to125 - vrefMIN_m40to125)/165/1.25
LET tempco_m30_85_ppmC=1e6*(vrefMAX_m30to85 - vrefMIN_m30to85)/115/1.25
**
PRINT tempco_m40_125_ppmC
PRINT tempco_m30_85_ppmC

print Iout25

.endc"}
C {simulator_commands_shown.sym} -290 -260 0 0 {
name=Libs_Ngspice
simulator=ngspice
only_toplevel=false
value="
.lib cornerMOSlv.lib mos_tt
.lib cornerMOShv.lib mos_tt
.lib cornerRES.lib res_typ
.lib cornerDIO.lib dio_tt
.lib cornerPNP.lib typ
"
      }
C {vsource.sym} 310 70 0 0 {name=Viout1 value=1 savecurrent=false}
C {sg13cmos5l_srout_tinybgr.sym} 10 0 0 0 {name=xbgrtop}
