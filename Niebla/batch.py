from os import system
for number in range(1,326+1):
    command = "convert -density 300 nieblanivola00unam.pdf[%d] pngs/%03d.png"%(number,number)
    print(command)
    system(command)
