import traceback
from util.log.mylog import log

def raiseout():
    log().debug( "This is a debug log.")
    with open(log().logname, 'a+') as f:
        f.writelines(traceback.format_exc())