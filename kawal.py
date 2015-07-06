import re, textwrap
import sys
import os
import random
import json
import ConfigParser
config = ConfigParser.ConfigParser()
config.readfp(open(r'/home/pi/.conf'))
sciezka = config.get('live','sciezka')


reload(sys)
sys.setdefaultencoding('UTF8')

c = '"'
s= ' '
source = sys.argv[1]
lines = open(sciezka + 'pliki/cytaty3.txt').read().splitlines()
myline =random.choice(lines)
#print(myline)
os.system("python " + sciezka + "sendtw.py " + source + s + c + myline + c)
os.system("python " + sciezka + "sendtw.py " + source + s + c + "koniec" + c)



