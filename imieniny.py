import urllib
from bs4 import BeautifulSoup
import sys
import os
import re
reload(sys)
sys.setdefaultencoding('UTF8')
c1 = '"'
s1= ' '
import ConfigParser
config = ConfigParser.ConfigParser()
config.readfp(open(r'/home/pi/.conf'))
sciezka = config.get('live','sciezka')



url = "http://www.kalbi.pl"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
source = sys.argv[1]

dzienr = soup.find("div", {"class": "calCard-head"})
dzienmc = soup.find("div", {"class": "calCard-day  satday"})
dzienn = soup.find("div", {"class": "calCard-day-week  satday"})
imieniny = soup.find("div", {"class": "calCard-name-day"})
przyslowie = soup.find("div", {"class": "calCard_proverb"})
nswieta = soup.find("div", {"class": "calCard-ententa"})
cytat = soup.find("div", {"class": "calCard-quotes"})


a = dzienr.getText()
b = dzienmc.getText()
c = dzienn.getText()
d = imieniny.getText()
e = przyslowie.getText()
f = nswieta.getText()
g = cytat.getText()


x = a + b + c + d  + e + f + g



xx = re.sub('\n*', '', x)
xy = re.sub('   ', '', xx) 
os.system("python " + sciezka + "sendtw.py " + source + s1 + c1 + xy +  c1)
