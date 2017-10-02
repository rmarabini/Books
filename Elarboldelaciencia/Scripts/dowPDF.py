from urllib.request import urlopen
import time
from functools import wraps

_init = 1

def retry(ExceptionToCheck, tries=4, delay=3, backoff=2, logger=None):
    """Retry calling the decorated function using an exponential backoff.

    http://www.saltycrane.com/blog/2009/11/trying-out-retry-decorator-python/
    original from: http://wiki.python.org/moin/PythonDecoratorLibrary#Retry

    :param ExceptionToCheck: the exception to check. may be a tuple of
        exceptions to check
    :type ExceptionToCheck: Exception or tuple
    :param tries: number of times to try (not retry) before giving up
    :type tries: int
    :param delay: initial delay between retries in seconds
    :type delay: int
    :param backoff: backoff multiplier e.g. value of 2 will double the delay
        each retry
    :type backoff: int
    :param logger: logger to use. If None, print
    :type logger: logging.Logger instance
    """
    def deco_retry(f):

        @wraps(f)
        def f_retry(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return f(*args, **kwargs)
                except ExceptionToCheck as e:
                    msg = "%s, Retrying in %d seconds..." % (str(e), mdelay)
                    if logger:
                        logger.warning(msg)
                    else:
                        print (msg)
                    time.sleep(mdelay)
                    mtries -= 1
                    mdelay *= backoff
            return f(*args, **kwargs)
        return f_retry  # true decorator
    return deco_retry

@retry(Exception, tries=4000,delay=300, backoff=1)
def run():

    #http://babel.hathitrust.org/cgi/imgsrv/download/pdf?
    # id=uc1.31175007204947;orient=0;size=100;seq=6;attachment=0

    #https://babel.hathitrust.org/cgi/imgsrv/download/pdf?
    # id=njp.32101076123619;orient=0;size=100;seq=5;attachment=0

    _localUbicacion=r"C:\Users\rm\Desktop\Boook\Elarboldelaciencia\raw"

    #_bookName="uc1.31175007204947"
    _bookName="njp.32101076123619"
    _remoteUbicacion="http://babel.hathitrust.org/cgi/imgsrv/download/pdf?id="
    _postFix=";orient=0;size=100;seq=%d;attachment=0"
    _remoteUrl = _remoteUbicacion+_bookName+_postFix
    _localUrl  = _localUbicacion+"\%03d.pdf"
    global _init
    #_init=20
    #_end=226+1
    _end=358 + 1
    for i in range(_init,_end):
        print (_remoteUrl%i)

        pdfFile = urlopen(_remoteUrl%i)
        output = open(_localUrl%i,'wb')
        output.write(pdfFile.read())
        output.close()
        time.sleep(2)
        _init += 1

        #http://babel.hathitrust.org/cgi/imgsrv/image?id=uc1.31175007204947;seq=226;width=759
        #http://babel.hathitrust.org/cgi/imgsrv/image?id=uiug.30112064052548;seq=12;width=759
        #http://babel.hathitrust.org/cgi/imgsrv/download/pdf?id=uiug.30112064052548;orient=0;size=100;seq=220;attachment=0

run()
