import re
import glob
import os

path = "no*.txt"
files = sorted(glob.glob(path))
counter=1

for file in files:
    fin  = open(file, 'r')
    text = fin.read() # in file
    fin.close()
    if counter==0:
        file2 = "a%03d.txt"%(counter+1)
    else:
        file2 = "%02d.txt"%counter

    fin  = open(file2, 'w')
    fin.write(text)
    fin.close()
    counter = counter + 1 
    print 'cp "%s" %s'%(file,file2)
    #os.system('diff "%s" %s'%(file,file2) )

