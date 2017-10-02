import re
import glob
import os

counter =1

for count in range(1,316):
    file1 = "%03d.png"%count
#    command = "convert %s  -gravity east -bordercolor white -extent $(identify -format '%%[fx:W+40]x%%H'  %s)  %s "%(file1,file1,file1)
    command = "convert %s  -gravity west -bordercolor white -extent $(identify -format '%%[fx:W+40]x%%H'  %s)  %s "%(file1,file1,file1)
    input_var = raw_input("Image %s, enter aply "%file1)
    if input_var: 
    	print "skip %s" % input_var
    else:
        print command
        os.system(command )

