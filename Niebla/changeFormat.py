import glob
import os
# now you can call it directly with basename
for filename in glob.glob('./*.ppm'):
    base_file, ext = os.path.splitext(filename)
    #os.rename(filename, base_file + ".text")
    command = "convert %s%s %s.png"%(base_file,ext,base_file) 
    print command
    os.system(command)
