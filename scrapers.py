#! /usr/bin/env python3
# Extract the crowd-level from boulderwelt-muenchen-ost.de

import re
import requests
import yaml
from bs4 import BeautifulSoup as bs


class Scraper(object):
    def __init__(self, tag):
        self.tag = tag

    def getCrowdLevel(self):
        '''
        Gets either the crowd level (a string, representing a numeral from
        0 to 100) or returns an error code
        - BADRXXX http request code was not 200. XXX is replaced by the code
        - N/A     the website didn't contain the data (happens when the building
                  is closed)
        '''
        raise NotImplementedError


class ScraperMO(Scraper):
    def __init__(self):
        super(ScraperMO, self).__init__("MO")

    def getCrowdLevel(self):
        r = requests.get('https://www.boulderwelt-muenchen-ost.de/')
        if not r.ok:
            return 'BADR%3d' % (r.status_code)

        soup = bs(r.text, features='lxml')

        item = soup.select_one('.crowd-level-tag > div')
        if not item:
            return 'N/A'

        levelStr = item.get_text()
        if not levelStr:
            return 'N/A'

        return int(levelStr[:-1])


class ScraperVauxwall(Scraper):
    def __init__(self):
        super(ScraperVauxwall, self).__init__("VAUXWALL")

    def getCrowdLevel(self):
        r = requests.get('https://portal.rockgympro.com/portal/public/a67951f8b19504c3fd14ef92ef27454d/occupancy?=&iframeid=occupancyCounter&fId=1277')
        if not r.ok:
            return 'BADR%3d' % (r.status_code)

        js = r.text
        regex_match = re.search("var data = ({.*?});", js, re.DOTALL)
        data = regex_match.group(1)
        try:
            return yaml.load(data)["VWS"]["count"]
        except KeyError:
            return 'N/A'
