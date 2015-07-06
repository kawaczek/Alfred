import urllib, re, time
import sys
import os
c = '"'
s= ' '

source = sys.argv[1]
www = urllib.urlopen('http://www.meteoprog.pl/pl/weather/' + sys.argv[2] )
www_tekst = www.read()
wyrazenie = '<meta property="og:description" content="(.+?)" />'
pogoda = re.findall(wyrazenie, www_tekst)
# pogoda[0]
os.system("python /home/pi/twitter/sendtw.py " + source + s + c + pogoda[0] +  c)
