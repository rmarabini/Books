import re
import glob
import os

path = "1914*.txt"
files = glob.glob(path)

for file in files:
    fin  = open(file, 'r')
    text = fin.read() # in file
    fin.close()
    file2 = file.replace("1914 - 0","")
    fin  = open(file2, 'w')
    fin.write(text)
    fin.close()
    #print 'diff "%s" %s'%(file,file2)
    os.system('diff "%s" %s'%(file,file2) )

