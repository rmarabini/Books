import re
import glob
import os

#path = "???.png"
path = "arbol*.txt"
files = sorted(glob.glob(path), reverse=False)
#counter=0
counter=1

for file in files:
#    file2 = "%03d.png"%(counter)
    file2 = "%03d.txt"%(counter)
    command = 'mv "%s" %s'%(file,file2) 
    print command
    counter += 1
    os.system(command)

