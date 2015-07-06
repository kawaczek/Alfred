import wit
import json
import sys
import requests
import os
import urllib, re, time
import re, textwrap
import ConfigParser
config = ConfigParser.ConfigParser()
config.readfp(open(r'/home/pi/.conf'))
sciezka = config.get('live','sciezka')
witapi = config.get ('api','witai')

reload(sys)
sys.setdefaultencoding('UTF8')

c = '"'
s= ' '
e1 = "nic"
e2 = "nic"
source = sys.argv[1]



wit.init()
response = wit.text_query(sys.argv[2], witapi)
z = json.loads(format(response))
wit.close()
intent = z["outcomes"][0]["intent"]
dane = z["outcomes"][0]["_text"]
print intent+dane
if intent == "szukaj":
 r = requests.get('http://searx.me/?format=json&q=%21go%20' + dane)
 z = r.json()
 w1 = z["results"][0]["content"]
 link = z["results"][0]["url"]
 os.system("python " + sciezka + "sendtw.py " + source + s + c + w1 +  c)
 os.system("python " + Sciezka + "sendtw.py " + source + s + c + link +  c)
if intent == "Pogoda":
 os.system("python " + sciezka + "pogoda.py " + source +  " gorzowwielkopolski")
if intent == "sentencja":
 os.system("python " + sciezka + "kawal.py " + source) 
