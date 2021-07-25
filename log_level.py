#! /usr/bin/env python3
# Continuously log the crowd-level of boulderwelt-muenchen-ost.de

import datetime
import logging
import pathlib
import time

import scrapers
from status_reporter import StatusReporter

INTERVAL = 15 * 60  # interval between log entries [s]


class Storage:
    def __init__(self):
        pathlib.Path('data/').mkdir(parents=True, exist_ok=True)

    def currentDataFileName(self):
        return 'data/%s.csv' % (datetime.date.today())

    def record(self, s):

        with open(self.currentDataFileName(), 'a') as logFile:
            logFile.write(s + '\n')



def recordCurrentLevel(storage, scraper):
    lvl = scraper.getCrowdLevel()
    storage.record('%s,%s,%s' % (scraper.tag, datetime.datetime.now(), lvl))


def runLogLoop(storage, scraper):
    while True:
        try:
            recordCurrentLevel(storage, scraper)
        except Exception as e:
            logging.exception(e)
        time.sleep(INTERVAL)


if __name__ == '__main__':

    appStart = datetime.datetime.now().strftime('%Y-%m-%dT%H.%M.%S')
    logging.basicConfig(
        format="%(asctime)s %(levelname)s %(message)s",
        filename="log/log_level-%s.log" % (appStart))

    reporter = StatusReporter("http://localhost:2048", "boulderlogger")
    reporter.start()
    scraper = scrapers.ScraperVauxwall()
    runLogLoop(Storage(), scraper)