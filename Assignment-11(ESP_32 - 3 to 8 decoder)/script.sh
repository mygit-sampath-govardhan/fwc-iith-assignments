#!/bin/bash

cd codes

pio run

pio run -t nobuild -t upload --upload-port 192.168.162.61

cd ..

pdflatex Assignment11.tex

termux-open Assignment11.pdf
