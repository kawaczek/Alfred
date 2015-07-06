import re, textwrap
import sys
import os
import random
import json
reload(sys)
sys.setdefaultencoding('UTF8')
os.system("bash /home/pi/twitter/burza.sh ")
c = '"'
s= ' '
source = sys.argv[1]
lines = open('/home/pi/twitter/pliki/burza').read().splitlines()
komunikat =  lines[0] + " promien 20 kilometrow, miejscowosc Gorzow Wielkopolski " + lines [1] + s + lines [2]
#print lines

#print(myline)
os.system("python /home/pi/twitter/sendtw.py " + source + s + c + komunikat + c)
#os.system("python /home/pi/twitter/sendtw.py " + source + s + c + "koniec" + c)



