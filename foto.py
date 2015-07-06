import sys
import time
import os
import ConfigParser
config = ConfigParser.ConfigParser()
config.readfp(open(r'/home/pi/.conf'))

sciezka = config.get('live','sciezka')

reload(sys)
sys.setdefaultencoding('UTF8')

timestamp = int(time.time())
source = sys.argv[1]
c = '"'
s= ' '

os.system("fswebcam -r 640x480 --save " + sciezka + "pliki/foto.png")
os.system("curl --upload-file " + sciezka + "pliki/foto.png https://transfer.sh/ >> " + sciezka + "pliki/fotki.txt")
with open(sciezka +'pliki/fotki.txt') as myfile:
    os.system("python " + sciezka + "sendtw.py " + source + s + c + (list(myfile)[-1]) +  c)
