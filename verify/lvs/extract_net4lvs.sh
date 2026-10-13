#!/usr/bin/bash
#
#
cd ../../magic
../scripts/extract_lvs.sh sg13cmos5l_srout_tinybgr
cp sg13cmos5l_srout_tinybgr.spice ../verify/lvs/sg13cmos5l_srout_tinybgr_lvs.spice
