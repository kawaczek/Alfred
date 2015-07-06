import urllib, re, time
import sys
import os
import ConfigParser
config = ConfigParser.ConfigParser()
config.readfp(open(r'/home/pi/.conf'))
sciezka = config.get('live','sciezka')


c = '"'
s= ' '

source = sys.argv[1]
www = urllib.urlopen('http://www.meteoprog.pl/pl/weather/' + sys.argv[2] )
www_tekst = www.read()
wyrazenie = '<meta property="og:description" content="(.+?)" />'
pogoda = re.findall(wyrazenie, www_tekst)
# pogoda[0]
os.system("python " + sciezka + "sendtw.py " + source + s + c + pogoda[0] +  c)
