#! /usr/bin/env python3
# Extract the crowd-level from boulderwelt-muenchen-ost.de

import requests
from bs4 import BeautifulSoup as bs

def getCrowdLevel():
    '''
    Gets either the crowd level (a string, representing a numeral from
    0 to 100) or returns an error code
    - BADRXXX http request code was not 200. XXX is replaced by the code
    - N/A     the website didn't contain the data (happens when the building
              is closed)
    '''
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

if __name__ == '__main__':
    print(getCrowdLevel())
