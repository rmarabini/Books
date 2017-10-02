import glob
import os
list1=range(8421,8506)
list2=range(8506,8590+1)
counter=1
# now you can call it directly with basename
for cont1, cont2 in zip(list1,list2):
    in_file1='/run/media/roberto/KINGSTON/138_FUJI/DSCF%d.JPG'%cont1
    in_file2='/run/media/roberto/KINGSTON/138_FUJI/DSCF%d.JPG'%cont2
    out_file1='/run/media/roberto/KINGSTON/138_FUJI/DSCF%03d.JPG'%counter
    counter = counter +1
    out_file2='/run/media/roberto/KINGSTON/138_FUJI/DSCF%03d.JPG'%counter
    command = "mv %s %s"%(in_file1,out_file1) 
    counter = counter +1
    print command
    os.system(command)
    command = "mv %s %s"%(in_file2,out_file2) 
    print command
    os.system(command)
