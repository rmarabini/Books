import re
import glob
import os

path = "???.png"
files = sorted(glob.glob(path))
counter=1

for file in files:
    #file2 =  file.replace("tif","png").replace("-000","")
    file2="%03d.png"%counter
    counter = counter + 1 
    print '"%s" %s'%(file,file2)
    os.system('convert "%s" -resize 1000      -depth 2 %s'%(file,file2) )

