#!/bin/bash

cd codes/GCC_Project
make 

scp output/bin/codes.bin sam-admin@192.168.99.238:/home/sam-admin/iith/arm     #transfers .bin file to pi

cd ..
cd ..
pdflatex Assignment9.tex
termux-open Assignment9.pdf
