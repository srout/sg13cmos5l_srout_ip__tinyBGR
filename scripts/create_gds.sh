#!/usr/bin/bash
#
#flatten -dotoplabels mytop_flat
#load mytop_flat
magic -dnull -noconsole -rcfile $PDK_ROOT/ihp-sg13cmos5l/libs.tech/magic/ihp-sg13cmos5l.magicrc << EOF
load $1
select top cell
gds contacts no
gds write $1.gds
quit -noprompt
EOF
