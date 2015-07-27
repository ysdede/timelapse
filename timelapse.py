#!/usr/bin/env python

import time
import picamera
from datetime import datetime
import os, errno

STARTHOUR = 14 # 0 - 23
ENDHOUR = 18   # 0 - 23
INTERVAL = 12 # Seconds
HFLIP = True
VFLIP = True
QUALITY = 22
THUMBNAILS = True

rotateCmd = ""
INVHOURS = False
thCmd = " -th none "


d = datetime.now()

HERE = os.path.abspath(os.path.dirname(__file__))
imagesFolder = HERE + '/Series/{}'.format(d.strftime('%d%m%Y'))

try:
	os.makedirs(imagesFolder)
	print "Created new directory: {}".format(imagesFolder)
except OSError as exc:
	if exc.errno == errno.EEXIST and os.path.isdir(imagesFolder):
		 print "Error: Can\'t create directory. Folder: {} already exits?".format(imagesFolder)

'''
try:
    os.mkdir(imagesFolder)
    print('Created new folder ' + imagesFolder)
except:
    print "Error: Can\'t create directory. Folder: {} already exits?".format(imagesFolder)
'''

print 'Start time: {}, End time: {}, Interval: {} seconds'.format(STARTHOUR, ENDHOUR, INTERVAL)

if (STARTHOUR > ENDHOUR):
   STARTHOUR, ENDHOUR, INVHOURS = ENDHOUR, STARTHOUR, True

while True:
   d = datetime.now()
   if (INVHOURS ^ (d.hour >= STARTHOUR and d.hour < ENDHOUR) and not d.second % INTERVAL):
      fileName = '{}/IMG{}.jpg'.format(imagesFolder, d.strftime('%d%H%M%S'))
      with picamera.PiCamera() as camera:
           camera.resolution = (1920, 1080)
           camera.hflip,  camera.vflip = HFLIP, VFLIP
           camera.sharpness = 20
           camera.contrast = 0
           camera.brightness = 50
           #camera.saturation = 0
           #camera.ISO = 0
           camera.video_stabilization = False
           #camera.exposure_compensation = 0
           camera.exposure_mode = 'auto'
           camera.meter_mode = 'average'
           camera.awb_mode = 'auto'
           camera.image_effect = 'none'
           camera.color_effects = None
           camera.capture(fileName)
           print 'Image created: {}'.format(fileName)
