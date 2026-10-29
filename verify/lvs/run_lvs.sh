#!/usr/bin/bash -f

#netgen -batch lvs "sg13cmos5l_srout_tinybgr.spice sg13cmos5l_srout_tinybgr" "sg13cmos5l_srout_tinybgr_lvs.spice sg13cmos5l_srout_tinybgr" /foss/pdks/ihp-sg13cmos5l/libs.tech/netgen/ihp-sg13cmos5l_setup.tcl lvs-report.out
#
#netgen -batch lvs "slot15_wrapper.spice slot15_wrapper" "slot15_wrapper_lvs.spice slot15_wrapper" /foss/pdks/ihp-sg13cmos5l/libs.tech/netgen/ihp-sg13cmos5l_setup.tcl lvs-report.out
netgen -batch lvs "slot15_wrapper.spice slot15_wrapper" "slot_15.spice slot_15" /foss/pdks/ihp-sg13cmos5l/libs.tech/netgen/ihp-sg13cmos5l_setup.tcl lvs-report.out
