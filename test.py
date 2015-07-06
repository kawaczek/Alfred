import wit
import json
import sys
import requests
import os
import urllib, re, time
import re, textwrap
reload(sys)
sys.setdefaultencoding('UTF8')

c = '"'
s= ' '
e1 = "nic"
e2 = "nic"
source = sys.argv[1]



wit.init()
response = wit.text_query(sys.argv[2], "AD7532EW76GPJQP5JMDB2A47SS747EW3")
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
 os.system("python /home/pi/twitter/sendtw.py " + source + s + c + w1 +  c)
 os.system("python /home/pi/twitter/sendtw.py " + source + s + c + link +  c)
if intent == "Pogoda":
 os.system("python ~/twitter/pogoda.py " + source +  " gorzowwielkopolski")
if intent == "sentencja":
 os.system("python ~/twitter/kawal.py " + source) 
