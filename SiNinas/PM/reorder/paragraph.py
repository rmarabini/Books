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
    text = re.compile("\r\nD. ").sub("\r\n\r\nD. ",text)
    text = text.replace("\r\nD.^{a}","\r\n\r\nD.^{a}")
    text = re.compile("\r\nSimon. ").sub("\r\n\r\nSimon. ",text)
    text = re.compile("\r\nRita. ").sub("\r\n\r\nRita. ",text)
    text = re.compile("\r\nCalam. ").sub("\r\n\r\nCalam. ",text)
    text = re.compile("\r\nESCENA").sub("\r\n\r\nESCENA",text)

    fin  = open(file, 'w')
    fin.write(text)
    fin.close()
    #counter = counter + 1 
    print 'process file %s'%file
    #os.system('diff "%s" %s'%(file,file2) )

