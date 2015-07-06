import re, textwrap
import sys
import os
import random
import json
reload(sys)
sys.setdefaultencoding('UTF8')

c = '"'
s= ' '
source = sys.argv[1]
lines = open('/home/pi/twitter/pliki/cytaty3.txt').read().splitlines()
myline =random.choice(lines)
#print(myline)
os.system("python /home/pi/twitter/sendtw.py " + source + s + c + myline + c)
os.system("python /home/pi/twitter/sendtw.py " + source + s + c + "koniec" + c)



