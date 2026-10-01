v {xschem version=3.4.8RC file_version=1.3}
G {}
K {}
V {}
S {}
F {}
E {}
P 4 1 -10 -540 {}
T {STARTUP CKT} -440 -10 0 0 0.2 0.2 {}
T {BANDGAP} 160 -10 0 0 0.2 0.2 {}
N 120 -100 140 -100 {lab=AVSS}
N 140 -100 140 -30 {lab=AVSS}
N 80 -30 140 -30 {lab=AVSS}
N 80 -70 80 -30 {lab=AVSS}
N 80 -540 80 -510 {lab=AVDD}
N 70 -480 80 -480 {lab=AVDD}
N 70 -540 70 -480 {lab=AVDD}
N 70 -540 80 -540 {lab=AVDD}
N 80 -390 150 -390 {lab=#net1}
N 80 -430 80 -390 {lab=#net1}
N 150 -390 150 -330 {lab=#net1}
N 120 -330 150 -330 {lab=#net1}
N 150 -480 150 -430 {lab=#net1}
N 120 -480 150 -480 {lab=#net1}
N -240 -420 -220 -420 {lab=AVSS}
N -240 -390 -240 -380 {lab=#net1}
N 80 -380 80 -360 {lab=#net1}
N -400 -540 -400 -510 {lab=AVDD}
N -410 -540 -400 -540 {lab=AVDD}
N -410 -480 -400 -480 {lab=AVDD}
N -410 -540 -410 -480 {lab=AVDD}
N -450 -540 -410 -540 {lab=AVDD}
N -360 -480 -340 -480 {lab=AVSS}
N -400 -450 -400 -230 {lab=vgsu1}
N -310 -420 -280 -420 {lab=vgsu1}
N 40 -330 80 -330 {lab=AVSS}
N -240 -540 -240 -450 {lab=AVDD}
N -400 -540 -240 -540 {lab=AVDD}
N -400 -230 -400 -210 {lab=vgsu1}
N -360 -180 -340 -180 {lab=AVSS}
N -440 -180 -400 -180 {lab=AVSS}
N -460 -30 -440 -30 {lab=AVSS}
N -400 -230 -310 -230 {lab=vgsu1}
N -310 -420 -310 -230 {lab=vgsu1}
N -440 -180 -440 -30 {lab=AVSS}
N -340 -30 80 -30 {lab=AVSS}
N -400 -150 -400 -30 {lab=AVSS}
N -440 -30 -400 -30 {lab=AVSS}
N 80 -300 80 -260 {lab=#net2}
N 80 -200 80 -130 {lab=Vbe2}
N 80 -430 150 -430 {lab=#net1}
N 80 -450 80 -430 {lab=#net1}
N -240 -540 70 -540 {lab=AVDD}
N -240 -380 80 -380 {lab=#net1}
N 80 -390 80 -380 {lab=#net1}
N -340 -480 -340 -180 {lab=AVSS}
N -340 -180 -340 -30 {lab=AVSS}
N -400 -30 -340 -30 {lab=AVSS}
C {sg13cmos5l_pr/pnpMPA.sym} 100 -100 0 1 {name=Q2
m=1
a=1.4p
p=5.4u}
C {sg13cmos5l_pr/sg13_hv_nmos.sym} 100 -330 0 1 {name=MN2
l=1u
w=2.6u
ng=1
m=1
}
C {sg13cmos5l_pr/sg13_hv_pmos.sym} 100 -480 0 1 {name=MP2
l=4u
w=1u
ng=1
m=1
}
C {iopin.sym} -450 -540 0 1 {name=p1 lab=AVDD}
C {iopin.sym} -460 -30 0 1 {name=p2 lab=AVSS}
C {lab_wire.sym} 40 -330 0 0 {name=p3 sig_type=std_logic lab=AVSS}
C {sg13cmos5l_pr/sg13_hv_nmos.sym} -260 -420 0 0 {name=MNSU1
l=2u
w=1u
ng=1
m=1
}
C {sg13cmos5l_pr/sg13_hv_pmos.sym} -380 -480 0 1 {name=MPSU1
l=6u
w=0.35u
ng=1
m=1
}
C {sg13cmos5l_pr/sg13_hv_nmos.sym} -380 -180 0 1 {name=MNSU2
l=1u
w=1u
ng=1
m=1
}
C {lab_wire.sym} -230 -420 0 1 {name=p13 sig_type=std_logic lab=AVSS}
C {lab_wire.sym} -310 -380 0 1 {name=p15 sig_type=std_logic lab=vgsu1}
C {lab_wire.sym} 80 -160 0 0 {name=p5 sig_type=std_logic lab=Vbe2}
C {sg13cmos5l_pr/rhigh.sym} 80 -230 0 0 {name=R27
l=4u
w=1.1u
m=1
body=AVSS}
