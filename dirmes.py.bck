import tweepy
import json
import os
import sys
import random
import ConfigParser
config = ConfigParser.ConfigParser()
config.readfp(open(r'/home/pi/.conf'))

consumer_key = config.get('twiter', 'consumer_key')
consumer_secret = config.get('twiter','consumer_secret')
access_token = config.get('twiter','access_token')
access_token_secret = config.get('twiter','access_token_secret')
sciezka = config.get('live','sciezka')
kawak = config.get('Wlasciciel', 'twid')
joanna = config.get('Joanna','twid')
jarrod = config.get('Jarrod','twid')

reload(sys)
sys.setdefaultencoding('UTF8')



c = '"'
s= ' '
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
auth.set_access_token(access_token, access_token_secret)  
api = tweepy.API(auth)  
error = tweepy.error.TweepError

class CustomStreamListener(tweepy.StreamListener):
  def on_direct_message(self,status):
    decoded = json.dumps(status._json)
    a = json.loads(decoded)
    source = a['direct_message']['sender_id_str']
    print  a['direct_message']['sender_screen_name'] + "(" + a["direct_message"]["sender_id_str"] + ")" + ": " + a['direct_message']['text'] 


    if  a['direct_message']['text'] in open(sciezka +'pliki/w.txt').read() and  a["direct_message"]["sender_id_str"] != "3340726557": 
	lines = open(sciezka + 'pliki/witaj.txt').read().splitlines()
	if  source == joanna:
         api.send_direct_message(user_id = source , text = random.choice(lines) + " Joanno" )
	else:
      	 api.send_direct_message(user_id = source , text = random.choice(lines) )
    else:
     if source == kawak:
          lines = open(sciezka + 'pliki/czekaj.txt').read().splitlines()
          es2 =  random.choice(lines)
          api.send_direct_message(user_id = source , text = es2 )
	  if a['direct_message']['text'] == "fotka":
             os.system("python " + sciezka +  "foto.py " + source)
          elif a['direct_message']['text'] == "Burza":
	     os.system("python " + sciezka +  "burza.py " +  source)
          else:
             os.system("python " + sciezka +  "test.py " +  source + s + c + a['direct_message']['text'] + c) 

     elif source == joanna:
          lines = open(sciezka + 'pliki/czekaj.txt').read().splitlines()
          es2 =  random.choice(lines)
          api.send_direct_message(user_id = source , text = es2 )
          if a['direct_message']['text'] == "fotka":
             os.system("python " + sciezka +  "foto.py " + source)
          elif a['direct_message']['text'] == "Burza":
             os.system("python " + sciezka +  "burza.py " +  source)
          else:
              os.system("python " + sciezka +  "test.py " +  source + s + c + a['direct_message']['text'] + c)

     elif source == jarrod :
      lines = open(sciezka + 'czekaj.txt').read().splitlines()
      es2 =  random.choice(lines)
      api.send_direct_message(user_id = source , text = es2 )
      os.system("python " + sciezka +  "test.py " +  source + s + c + a['direct_message']['text'] + c)

stream = tweepy.streaming.Stream(auth, CustomStreamListener())
streamuser = stream.userstream()
track_list = None
stream.filter( track_list)
