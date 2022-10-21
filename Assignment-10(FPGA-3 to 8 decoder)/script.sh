#!/bin/bash

ql_symbiflow -compile -src /sdcard/Download/iith/iith/vaman/Assignment-10/codes -d ql-eos-s3 -P PU64 -v Assignment10.v -t helloworldfpga -p Mypins.pcf -dump binary

scp /sdcard/Download/iith/iith/vaman/Assignment-10/codes/helloworldfpga.bin sam-admin@192.168.28.238:/home/sam-admin/iith/vaman/fpga


pdflatex Assignment10.tex

termux-open Assignment10.pdf

