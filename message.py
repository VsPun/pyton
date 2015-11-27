#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mraa
import urllib2
import time

DID = 'put_did_here'

URL_BASE = "http://168.63.82.20/server/income/?did=%s&action=put&value=" % DID

while True:
    # get message from some function
    msg = get_message_from_somethere()
    if msg:
        # send data to GO PLUS PLATFORM
        url = URL_BASE + msg
        try:
            urllib2.urlopen(url)
        except urllib2.HTTPError as e:
            if e.code == '404':
                print("URL not found: %s" % url)

    # sleep for 60 seconds
    time.sleep(60)
