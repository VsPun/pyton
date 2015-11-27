#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import print_function

import requests
from base64 import b64encode

DID = 'put_did_here'
URL_BASE = "http://168.63.82.20/server/getimage"


while True:
    # Make photo and save to some file, save its name to "filename" variable
    filename = get_filename_photo()
    if filename:
        # send photo to GO+ platform
        data = {
            'did' : DID,
            'image' : b64encode(open(filename, 'rb').read()),
               }
        r = requests.post(URL_BASE, data=data)

    # sleep for 60 seconds
    time.sleep(60)
