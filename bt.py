#!/usr/bin/env python
# coding: utf-8

import re, textwrap
import sys
import os
import random
import json

import time
from time import gmtime, strftime
reload(sys)
sys.setdefaultencoding('UTF8')
c = '"'
s= ' '
#time = 10
send = 0
#source = sys.argv[1]


def executeSomething():
    os.system("bash /home/pi/twitter/burza.sh ")
    lines = open('/home/pi/twitter/pliki/burza').read().splitlines()
    komunikat =  lines[0] + s + lines [1] + s + lines [2]

    if lines[0] == "Nie zarejestrowano wyładowań atmosferycznych w ciągu ostatnich 10 minut w wybranym promieniu dla wskazanej lokalizacji." or lines[0] == "Nie zarejestrowano wyładowań atmosferycznych w ciągu ostatnich 20 minut w wybranym promieniu dla wskazanej lokalizacji." or lines[0] == "Nie zarejestrowano wyładowań atmosferycznych w ciągu ostatnich 15 minut w wybranym promieniu dla wskazanej lokalizacji.":
       print komunikat
#       time.sleep(10) 
#       os.system("python /home/pi/twitter/sendtw.py " + 1690435358 + s + c + komunikat + c)
     # os.system("python /home/pi/twitter/sendtw.py " + 379322713 + s + c + komunikat + c) 
    else:
         os.system("python /home/pi/twitter/sendtw.py " + "1690435358" + s + c + komunikat + c)
         os.system("python /home/pi/twitter/sendtw.py " + "379322713" + s + c + komunikat + c)
 
         print komunikat
         print "time.sleep(10)"
    time.sleep(600)  
while True:
    executeSomething()



