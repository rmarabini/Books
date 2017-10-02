import re
import glob

path = "*.txt"
files = glob.glob(path)

for file in files:
    fin  = open(file, 'r')
    text = fin.read() # in file
    fin.close()
    p = re.compile(r'-([^\r])') # pattern
    newline = p.sub(r'--\1',text) # replace matching strings double dash
    fin  = open(file, 'w')
    fin.write(newline)
    fin.close()
