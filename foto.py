import sys
import time
import os
reload(sys)
sys.setdefaultencoding('UTF8')

timestamp = int(time.time())
source = sys.argv[1]
c = '"'
s= ' '

os.system("fswebcam -r 640x480 --save /home/pi/twitter/pliki/foto.png")
os.system("curl --upload-file /home/pi/twitter/pliki/foto.png https://transfer.sh/ >> /home/pi/twitter/pliki/fotki.txt")
with open('/home/pi/twitter/pliki/fotki.txt') as myfile:
    os.system("python /home/pi/twitter/sendtw.py " + source + s + c + (list(myfile)[-1]) +  c)
