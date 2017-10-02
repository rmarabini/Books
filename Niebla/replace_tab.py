import re
import glob

path = "*.txt"
files = sorted(glob.glob(path))

for file in files:
    fin  = open(file, 'r')
    text = fin.read() # in file
    fin.close()
    p = re.compile(r'\t') # pattern-> tab
    match = p.search(text)
    if match:
	print "file ", file, "has a tab"
    newline = p.sub(r' ',text) # replace matching strings with space
    fin  = open(file, 'w')
    fin.write(newline)
    fin.close()
