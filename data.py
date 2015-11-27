#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import time

DID = 'put_did_here'

URL_BASE = "http://168.63.82.20/server/income/?did=%s&action=put&value=" % DID

while True:
    # read value from some function
    value = read_data()
    if value:
        # send data to GO PLUS PLATFORM
        url = URL_BASE + value
        try:
            urllib2.urlopen(url)
        except urllib2.HTTPError as e:
            if e.code == '404':
                print("URL not found: %s" % url)

    # sleep for 60 seconds
    time.sleep(60)
