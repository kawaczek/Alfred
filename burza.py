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
os.system("bash " + sciezka + "burza.sh ")
c = '"'
s= ' '
source = sys.argv[1]
lines = open(sciezka +'pliki/burza').read().splitlines()
komunikat =  lines[0] + " promien 20 kilometrow, miejscowosc Gorzow Wielkopolski " + lines [1] + s + lines [2]
os.system("python " + sciezka +"sendtw.py " + source + s + c + komunikat + c)



