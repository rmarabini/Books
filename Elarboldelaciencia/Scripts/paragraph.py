import re
import glob
import os

path = "???.txt"
files = sorted(glob.glob(path))

#source="(\w+)-\n(\S*)"
source="\r\n  "
target="\r\n\r\n"

for file in files:
    fin  = open(file, 'r')
    text = fin.read() # in file
    fin.close()
    text = re.compile(source).sub(target,text)

    fin  = open(file, 'w')
    fin.write(text)
    fin.close()
    #counter = counter + 1 
    print 'process file %s'%file
    os.system('diff %s tmp/%s'%(file,file) )

