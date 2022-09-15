#!/bin/bash


#Download python and latex templates

#svn co https://github.com/gadepall/training/trunk/math  /home/iith

#Test Latex Installation
#Uncomment only the following lines and comment the above line

cd /home/iith 
texfot pdflatex gvv_math_eg.tex
cat gvv_math_eg.tex


#Test Python Installation
#Uncomment only the following line
#python3 /data/data/com.termux/files/home/storage/shared/training/math/codes/tri_sss.py

