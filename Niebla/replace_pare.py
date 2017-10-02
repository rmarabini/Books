# -*- coding: latin-1 -*-
import re
import glob

path = "*.txt"
files = glob.glob(path)

for file in files:
    fin  = open(file, 'r')
    text = fin.read() # in file
    fin.close()
    p = re.compile(r'\(\(') # pattern
    newline = p.sub(r'«',text) # replace matching strings double dash
    p = re.compile(r'\)\)') # pattern
    newline = p.sub(r'»',newline) # replace matching strings double dash
    fin  = open(file, 'w')
    fin.write(newline)
    fin.close()
