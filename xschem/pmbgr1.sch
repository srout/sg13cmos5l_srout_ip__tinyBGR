v {xschem version=3.4.8RC file_version=1.3}
G {}
K {}
V {}
S {}
F {}
E {}
P 4 1 -10 -540 {}
T {R1: 1.1u/351.5u 451.1k
R2: 1.1u/25u 32.2k
R1/R2=14.0
MP1: 4X1u/4u
MN1: 8X2u/1u
tempco: ~5ppm/C} -230 -140 0 0 0.2 0.2 {}
N 120 -100 140 -100 {lab=AVSS}
N 140 -100 140 -30 {lab=AVSS}
N 80 -30 140 -30 {lab=AVSS}
N 80 -70 80 -30 {lab=AVSS}
N 280 -30 340 -30 {lab=AVSS}
N 340 -70 340 -30 {lab=AVSS}
N 280 -100 300 -100 {lab=AVSS}
N 280 -100 280 -30 {lab=AVSS}
N 340 -180 340 -130 {lab=Vbe1}
N 80 -390 80 -360 {lab=Vgn}
N 340 -410 340 -360 {lab=#net1}
N 80 -540 80 -510 {lab=AVDD}
N 340 -540 340 -510 {lab=AVDD}
N 70 -480 80 -480 {lab=AVDD}
N 70 -540 70 -480 {lab=AVDD}
N 70 -540 80 -540 {lab=AVDD}
N 330 -480 350 -480 {lab=AVDD}
N 350 -540 350 -480 {lab=AVDD}
N 340 -540 350 -540 {lab=AVDD}
N -250 -30 80 -30 {lab=AVSS}
N 60 -330 80 -330 {lab=AVSS}
N 340 -330 360 -330 {lab=AVSS}
N 140 -30 280 -30 {lab=AVSS}
N 80 -540 340 -540 {lab=AVDD}
N 270 -480 300 -480 {lab=#net1}
N 270 -480 270 -410 {lab=#net1}
N 270 -410 340 -410 {lab=#net1}
N 340 -420 340 -410 {lab=#net1}
N 80 -390 150 -390 {lab=Vgn}
N 80 -450 80 -390 {lab=Vgn}
N 150 -390 150 -330 {lab=Vgn}
N 120 -330 150 -330 {lab=Vgn}
N -80 -540 70 -540 {lab=AVDD}
N 60 -330 60 -280 {lab=AVSS}
N 80 -210 80 -130 {lab=Vbe2}
N 360 -330 360 -290 {lab=AVSS}
N 340 -300 340 -240 {lab=Vbe2_cp}
N 650 -540 650 -510 {lab=AVDD}
N 520 -540 650 -540 {lab=AVDD}
N 510 -540 510 -510 {lab=AVDD}
N 350 -540 510 -540 {lab=AVDD}
N 510 -480 520 -480 {lab=AVDD}
N 520 -540 520 -480 {lab=AVDD}
N 510 -540 520 -540 {lab=AVDD}
N 650 -480 660 -480 {lab=AVDD}
N 660 -540 660 -480 {lab=AVDD}
N 650 -540 660 -540 {lab=AVDD}
N 340 -420 440 -420 {lab=#net1}
N 340 -450 340 -420 {lab=#net1}
N 440 -480 440 -420 {lab=#net1}
N 440 -480 470 -480 {lab=#net1}
N 440 -420 580 -420 {lab=#net1}
N 580 -480 580 -420 {lab=#net1}
N 580 -480 610 -480 {lab=#net1}
N 510 -450 510 -390 {lab=IOUT1}
N 650 -450 650 -390 {lab=IOUT2}
N -80 -540 -80 -510 {lab=AVDD}
N -90 -540 -80 -540 {lab=AVDD}
N 150 -480 150 -430 {lab=Vgp}
N 120 -480 150 -480 {lab=Vgp}
N -10 -430 150 -430 {lab=Vgp}
N -10 -480 -10 -430 {lab=Vgp}
N -40 -480 -10 -480 {lab=Vgp}
N -90 -480 -80 -480 {lab=AVDD}
N -90 -540 -90 -480 {lab=AVDD}
N -250 -540 -90 -540 {lab=AVDD}
N -80 -210 80 -210 {lab=Vbe2}
N 80 -300 80 -210 {lab=Vbe2}
N -170 -340 -80 -340 {lab=VREF}
N -80 -340 -80 -300 {lab=VREF}
N -80 -240 -80 -210 {lab=Vbe2}
N -80 -450 -80 -340 {lab=VREF}
N 280 -330 300 -330 {lab=#net2}
N 150 -330 220 -330 {lab=Vgn}
N 150 -480 200 -480 {lab=Vgp}
N 260 -480 270 -480 {lab=#net1}
C {sg13cmos5l_pr/pnpMPA.sym} 320 -100 0 0 {name=Q1
m=8
a=1.4p
p=5.4u}
C {sg13cmos5l_pr/pnpMPA.sym} 100 -100 0 1 {name=Q2
m=1
a=1.4p
p=5.4u}
C {sg13cmos5l_pr/sg13_hv_nmos.sym} 100 -330 0 1 {name=MN2
l=1u
w=2u
ng=1
m=4
}
C {sg13cmos5l_pr/sg13_hv_nmos.sym} 320 -330 0 0 {name=MN1
l=1u
w=2u
ng=1
m=8
}
C {sg13cmos5l_pr/sg13_hv_pmos.sym} 100 -480 0 1 {name=MP2
l=4u
w=1u
ng=1
m=2
}
C {sg13cmos5l_pr/sg13_hv_pmos.sym} 320 -480 0 0 {name=MP1
l=4u
w=1u
ng=1
m=4
}
C {iopin.sym} -250 -540 0 1 {name=p1 lab=AVDD}
C {iopin.sym} -250 -30 0 1 {name=p2 lab=AVSS}
C {lab_wire.sym} 80 -180 0 0 {name=p5 sig_type=std_logic lab=Vbe2}
C {lab_wire.sym} 340 -150 0 0 {name=p6 sig_type=std_logic lab=Vbe1}
C {lab_wire.sym} 340 -270 0 0 {name=p7 sig_type=std_logic lab=Vbe2_cp}
C {lab_wire.sym} 190 -330 0 0 {name=p8 sig_type=std_logic lab=Vgn}
C {lab_wire.sym} 180 -480 0 0 {name=p9 sig_type=std_logic lab=Vgp}
C {opin.sym} -170 -340 0 1 {name=p10 lab=VREF}
C {opin.sym} 510 -390 3 1 {name=p11 lab=IOUT1}
C {opin.sym} 650 -390 3 1 {name=p12 lab=IOUT2}
C {sg13cmos5l_pr/rhigh.sym} 340 -210 0 0 {name=R2
l=25u
w=1.1u
m=1
body=AVSS}
C {lab_wire.sym} 60 -280 0 0 {name=p3 sig_type=std_logic lab=AVSS}
C {lab_wire.sym} 360 -290 0 1 {name=p4 sig_type=std_logic lab=AVSS}
C {sg13cmos5l_pr/sg13_hv_pmos.sym} 490 -480 0 0 {name=MP3
l=4u
w=1u
ng=1
m=4
}
C {sg13cmos5l_pr/sg13_hv_pmos.sym} 630 -480 0 0 {name=MP4
l=4u
w=1u
ng=1
m=4
}
C {sg13cmos5l_pr/sg13_hv_pmos.sym} -60 -480 0 1 {name=MP5
l=4u
w=1u
ng=1
m=2
}
C {sg13cmos5l_pr/rhigh.sym} -80 -270 0 0 {name=R1
l=351.5u
w=1.1u
m=1
body=AVSS}
C {vsource.sym} 250 -330 1 0 {name=V1 value=PAR_NOFF savecurrent=false}
C {vsource.sym} 230 -480 1 0 {name=V2 value=PAR_POFF savecurrent=false}
