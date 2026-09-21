v {xschem version=3.4.8RC file_version=1.3}
G {}
K {}
V {}
S {}
F {}
E {}
N -300 -40 -300 -30 {lab=AVDD5V}
N -300 -40 -140 -40 {lab=AVDD5V}
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
C {vsource.sym} -300 0 0 0 {name=Vsup value="DC PAR_VDD5 AC 1 0" savecurrent=false}
C {gnd.sym} -300 70 0 0 {name=l1 lab=0}
C {capa.sym} 380 70 0 0 {name=C3
m=1
value=10f
footprint=1206
device="ceramic capacitor"}
C {lab_wire.sym} -200 -40 0 0 {name=p1 sig_type=std_logic lab=AVDD5V}
C {gnd.sym} 290 130 0 0 {name=l2 lab=0}
C {lab_wire.sym} 260 -20 0 0 {name=p2 sig_type=std_logic lab=VREF}
C {lab_wire.sym} 260 0 0 0 {name=p3 sig_type=std_logic lab=IOUT1}
C {devices/code_shown.sym} -330 150 0 0 {name=spcom only_toplevel=false value=".option savecurrents
.save all onoise_spectrum
.PARAM PAR_VDD5=3.3
.PARAM PAR_POFF=0
.PARAM PAR_NOFF=0
.TEMP 27

* .MEASURE AC PSR100 FIND VDB(VREF) AT=100
* .MEASURE AC PSR10k  FIND VDB(VREF) AT=1e4
* .MEASURE AC PSR100M FIND VDB(VREF) AT=1e8

.NOISE V(VREF) Vsup DEC 10 10 1e4

.print onoise_total

.control
run
save all

**Transient
* AC DEC 10 10 1e8


* PLOT ONOISE_SPECTRUM xlog
* PLOT VDB(VREF)

.endc"}
C {simulator_commands_shown.sym} -290 -260 0 0 {
name=Libs_Ngspice
simulator=ngspice
only_toplevel=false
value="
.lib cornerMOSlv.lib mos_tt
.lib cornerMOShv.lib mos_ss
.lib cornerRES.lib res_typ
.lib cornerDIO.lib dio_tt
.lib cornerPNP.lib typ
"
      }
C {vsource.sym} 310 70 0 0 {name=Viout1 value=1 savecurrent=false}
C {sg13cmos5l_srout_tinybgr.sym} 10 0 0 0 {name=xbgrtop}
