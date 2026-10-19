#!/usr/bin/bash
#
magic -dnull -noconsole -rcfile $PDK_ROOT/ihp-sg13cmos5l/libs.tech/magic/ihp-sg13cmos5l.magicrc << EOF
load $1
select top cell
flatten -dotoplabels mytop_flat
load mytop_flat
gds contacts no
gds write mytop_flat.gds
quit -noprompt
EOF
