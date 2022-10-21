#!/bin/bash

sudo python3 /home/sam-admin/iith/vaman/fpga/TinyFPGA-Programmer-Application/tinyfpga-programmer-gui.py --port /dev/ttyACM0 --appfpga helloworldfpga.bin --mode fpga --reset
