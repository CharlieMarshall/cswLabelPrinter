#!/usr/bin/env python2.7
import os, sys, datetime
# have to copy PIL to the /usr/local/lib/python2.7 folder
#sys.path.append("/usr/local/lib/python2.7/site-packages")
from PIL import Image, ImageDraw, ImageFont

now = datetime.datetime.now()
line1 = "SITE:\t\t\t27000247\t\t\t" + "DATE:\t\t\t" + now.strftime("%d-%m-%Y\t%H:%M")
line2 = "SAMPLE:\t\t\t" + sys.argv[1]

# create image
img = Image.new('RGB', (696, 100), color = 'white')
d = ImageDraw.Draw(img)

# requires a ttf font file 
fnt = ImageFont.truetype('/home/pi/bin/font/roboto/Roboto-Black.ttf', 30)
d.text((10,10), line1, font=fnt, fill=(0,0,0))
d.text((10,50), line2, font=fnt, fill=(0,0,0))

img.save('/home/pi/bin/image.png')

# print two copies
os.system("python /usr/local/lib/python2.7/site-packages/brother_ql/brother_ql_create.py --model QL-820NWB --label-size 62 --red /home/pi/bin/image.png > /home/pi/bin/output.bin && nc -q 1 192.168.101.17 9100 < /home/pi/bin/output.bin")
os.system("python /usr/local/lib/python2.7/site-packages/brother_ql/brother_ql_create.py --model QL-820NWB --label-size 62 --red /home/pi/bin/image.png > /home/pi/bin/output.bin && nc -q 1 192.168.101.17 9100 < /home/pi/bin/output.bin")
