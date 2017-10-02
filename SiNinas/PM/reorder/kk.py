import re
import glob
import os

path = "??.txt"
files = sorted(glob.glob(path), reverse=True)
#counter=0
counter=62

for file in files:
    fin  = open(file, 'r')
    text = fin.read() # in file
    fin.close()
    file2 = "p%s"%(file)
    fin  = open(file2, 'w')
    fin.write(text)
    fin.close()
    print 'mv "%s" %s'%(file,file2)
    #os.system('diff "%s" %s'%(file,file2) )

