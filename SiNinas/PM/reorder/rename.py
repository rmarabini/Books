import re
import glob
import os

path = "??.png"
files = sorted(glob.glob(path), reverse=True)
#counter=0
counter=62

for file in files:
    fin  = open(file, 'r')
    text = fin.read() # in file
    fin.close()
    if counter<56:
        break
    else:
        file2 = "%02d.png"%(counter+1)

    fin  = open(file2, 'w')
    #fin.write(text)
    fin.close()
    counter = counter - 1 
    print 'mv "%s" %s'%(file,file2)
    #os.system('diff "%s" %s'%(file,file2) )

