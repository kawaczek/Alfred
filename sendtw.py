#!/usr/bin/env python
# coding: utf-8

import tweepy
import json
import os
import sys
import textwrap
reload(sys)
sys.setdefaultencoding('UTF8')
import ConfigParser
config = ConfigParser.ConfigParser()
config.readfp(open(r'/home/pi/.conf'))

consumer_key = config.get('twiter', 'consumer_key')
consumer_secret = config.get('twiter','consumer_secret')
access_token = config.get('twiter','access_token')
access_token_secret = config.get('twiter','access_token_secret')
sciezka = config.get('live','sciezka')




auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
auth.set_access_token(access_token, access_token_secret)  
api = tweepy.API(auth)  
source =  sys.argv[1]
tekst =  sys.argv[2]
a = textwrap.wrap(tekst,130)
d = json.dumps(a)
d1 = json.loads(d)
dl = len(d1)



try:
 for i in range(dl):
	api.send_direct_message(user_id = source , text = a[i])

#api.send_direct_message(user_id = source , text = ".")


except tweepy.error.TweepError:
        pass





