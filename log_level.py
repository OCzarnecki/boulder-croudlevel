#! /usr/bin/env python3
# Continuously log the crowd-level of boulderwelt-muenchen-ost.de

import datetime
import pathlib
import time

from get_level import getCrowdLevel

INTERVAL = 15 * 60  # interval between log entries [s]
LOG_DIR  = 'log/'

class Logger:
    def __init__(self, logDir):
        self.logDir = logDir if logDir[-1] == '/' else logDir + '/'
        pathlib.Path(logDir).mkdir(parents=True, exist_ok=True)
        
    def logFileForNow(self):
        return '%s%s.log' % (self.logDir, datetime.date.today())
        
    def log(self, s):
        with open(self.logFileForNow(), 'a') as logFile:
            logFile.write(s + '\n')

def logCurrentLevel(logger):
    lvl = getCrowdLevel()
    logger.log('%s,%s' % (datetime.datetime.now(), lvl))
    
def runLogLoop(logger):
    while True:
        logCurrentLevel(logger)
        time.sleep(INTERVAL)
        
    
if __name__ == '__main__':
    runLogLoop(Logger(LOG_DIR))
