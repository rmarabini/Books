import re
import glob
import os

path = "??.txt"
#path = "kk.txt"
files = sorted(glob.glob(path))

#source="(\w+)-\n(\S+ )"
source="M O R A T I N\r\n"
target=""

for file in files:
    fin  = open(file, 'r')
    text = fin.read() # in file
    fin.close()
    text = re.compile("^D.a ").sub("D.^{a} ",text)
    text = re.compile("\r\nD.a ").sub("\r\nD.^{a} ",text)

    fin  = open(file, 'w')
    fin.write(text)
    fin.close()
    #counter = counter + 1 
    print 'process file %s'%file
    #os.system('diff "%s" %s'%(file,file2) )

