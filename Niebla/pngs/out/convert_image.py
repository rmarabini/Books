import re
import glob
import os

path = "???.tif"
files = sorted(glob.glob(path))
counter=1

for file in files:
    file2 = "%03d.png"%counter
    counter = counter + 1 
    print '"%s" %s'%(file,file2)
    os.system('convert "%s" -resize 1000      -depth 2 %s'%(file,file2) )

