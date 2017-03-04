#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config

import tweepy
import random
from datetime import datetime

import pprint
pp = pprint.PrettyPrinter(indent=4)


auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_key, config.access_secret)
api = tweepy.API(auth)


month_map = {
    '1': 'January',
    '2': 'February',
    '3': 'March',
    '4': 'April',
    '5': 'May',
    '6': 'June',
    '7': 'July',
    '8': 'August',
    '9': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December'
}


messages = [
    'Happy day!',
    'Have a nice day!',
    'How\'s your day going?',
    'One of the best days of the year!',
    'Remember to smile today!',
    'Today is yesterday\'s tomorrow!',
    'Today will be tomorrow\'s yesterday!',
    'Another day!',
    'Today is great!',
    'What\'s the news today?',
    'The week\'s going by so fast! Enjoy today!',
    'Enjoy your time on this earth. Especially today!'
]


# get current date string
datetime_now = datetime.now()

month_int = datetime_now.strftime('%m')
month_str = month_map[str(int(month_int))]

day_int = datetime_now.strftime('%d')
day_str = str(int(day_int))


# construct wiki url
wiki_link = 'https://en.wikipedia.org/wiki/' + month_str + '_' + day_str


# commit tweet
tweet_components = [
    random.choice(messages),
    month_str,
    day_str + ':',
    wiki_link
]

api.update_status(' '.join(tweet_components))





