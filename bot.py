#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config

import tweepy
import time
import sys


auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_key, config.access_secret)
api = tweepy.API(auth)


argfile = str(sys.argv[1])


with open(argfile,'r') as filename:
    f = filename.readlines()

for line in f:
    api.update_status(line)
    time.sleep(10)
