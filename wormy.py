#!/usr/bin/env python

import os 
from shutil import copyfile

for i in range(0,50):
    dst = '../wormy' +str(i) +'.py'
    copyfile('./wormy.py',dst)
