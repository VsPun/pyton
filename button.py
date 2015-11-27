#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mraa
import urllib2
import time

DID = 'put_did_here'

URL_BASE_INC = "http://168.63.82.20/server/income/?did=%s&action=inc" % DID
URL_BASE_DEC = "http://168.63.82.20/server/income/?did=%s&action=dec" % DID
while True:
    # get action from some function
    action = 'inc'
    if action == 'inc':
        # send data to GO PLUS PLATFORM
        url = URL_BASE_INC
        
    else if action == 'dec':
        # send data to GO PLUS PLATFORM
        url = URL_BASE_DEC
        
        try:
            urllib2.urlopen(url)
        except urllib2.HTTPError as e:
            if e.code == '404':
                print("URL not found: %s" % url)
    
    # sleep for 1 second
    time.sleep(1)
