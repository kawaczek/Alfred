#!/usr/bin/env python
# coding: utf-8

import re, textwrap
import sys
import os
import random
import json

import time
from time import gmtime, strftime
import ConfigParser
config = ConfigParser.ConfigParser()
config.readfp(open(r'/home/pi/.conf'))

kawak = config.get('Wlasciciel', 'twid')
sciezka = config.get('live','sciezka')


reload(sys)
sys.setdefaultencoding('UTF8')
c = '"'
s= ' '
#time = 10
send = 0
#source = sys.argv[1]


def executeSomething():
    os.system("bash " + sciezka + "burza.sh ")
    lines = open(sciezka + 'pliki/burza').read().splitlines()
    komunikat =  lines[0] + s + lines [1] + s + lines [2]

    if lines[0] == "Nie zarejestrowano wyładowań atmosferycznych w ciągu ostatnich 10 minut w wybranym promieniu dla wskazanej lokalizacji." or lines[0] == "Nie zarejestrowano wyładowań atmosferycznych w ciągu ostatnich 20 minut w wybranym promieniu dla wskazanej lokalizacji." or lines[0] == "Nie zarejestrowano wyładowań atmosferycznych w ciągu ostatnich 15 minut w wybranym promieniu dla wskazanej lokalizacji.":
        print komunikat
    else:
        os.system("python " + sciezka + "sendtw.py " + kawak + s + c + komunikat + c) 
        print komunikat
        print "time.sleep(10)"
    time.sleep(600)  
while True:
    executeSomething()



