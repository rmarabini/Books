from urllib.request import urlopen
import time, sys
from functools import wraps

_init = 1
def run():

    _localUbicacion=r"/home/roberto/sda/PGDP/Book/TwoWorlds/Images"
    _remoteUbicacion="http://www.chlt.org/sandbox/lhl/Salusbury/images/1440x1920/%d.jpg"
    _remoteUrl = _remoteUbicacion
    _localUrl  = _localUbicacion+"/%03d.jpg"
    global _init
    _init=3232
    #_end=226+1
    _end=3689 + 1
    for i in range(_init,_end):
        try:
          print (_remoteUrl%i)

          pdfFile = urlopen(_remoteUrl%i)
          output = open(_localUrl%i,'wb')
          output.write(pdfFile.read())
          output.close()
          time.sleep(2)
          _init += 1
        except:
          os.system(_localUrl%i)
          print ("Unexpected error:", sys.exc_info()[0])

        #http://babel.hathitrust.org/cgi/imgsrv/image?id=uc1.31175007204947;seq=226;width=759
        #http://babel.hathitrust.org/cgi/imgsrv/image?id=uiug.30112064052548;seq=12;width=759
        #http://babel.hathitrust.org/cgi/imgsrv/download/pdf?id=uiug.30112064052548;orient=0;size=100;seq=220;attachment=0

run()
