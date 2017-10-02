import re
import glob
import os

counter =1

for count in range(1,356 +1):
    file1 = "%03d.pdf"%count
#    command = "convert %s  -gravity east -bordercolor white -extent $(identify -format '%%[fx:W+40]x%%H'  %s)  %s "%(file1,file1,file1)
    #command = "convert %s  -crop 1000x1800+100+120 %s "%(file1,file1.replace("pdf","png"))    
    command = "pdfimages -png %s   %s "%(file1,file1[0:3])
    print (command) 
    os.system(command )
    fin  = file1[0:3]+"-000.png"
    fout = file1[0:3]+".png"
#RECOMPUTE RIGHT CROP
#RUN IN BOTH DIRECTORIES
    command = "convert %s  -crop 1150x1800+45+120 %s "%(fin,fout)    
    os.system(command )
#after OCR convert 21 but depth
os.system("rm ???-00[0-6].png" )



