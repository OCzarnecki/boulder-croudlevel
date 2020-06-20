#! /usr/bin/env python
# Extract the crowd-level from boulderwelt-muenchen-ost.de

import requests
from bs4 import BeautifulSoup as bs

def getCrowdLevel():
    r = requests.get('https://www.boulderwelt-muenchen-ost.de/')
    soup = bs(r.text, features='lxml')

    item = soup.select_one('.crowd-level-tag > div')
    
    levelStr = item.get_text()
    
    return int(levelStr[:-1])

if __name__ == '__main__':
    print(getCrowdLevel())
