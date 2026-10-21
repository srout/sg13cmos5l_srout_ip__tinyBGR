#!/usr/bin/bash
#
#flatten -dotoplabels mytop_flat
#load mytop_flat
PDK_ROOT=/foss/pdks
PDK=ihp-sg13cmos5l
PDKPATH=/foss/pdks/ihp-sg13cmos5l
magic -dnull -noconsole -rcfile $PDK_ROOT/ihp-sg13cmos5l/libs.tech/magic/ihp-sg13cmos5l.magicrc << EOF
drc off
drc style drc(full)
load $1
select top cell
expand
drc on
drc check
drc catchup
EOF
