#!/usr/bin/env python
#-*- coding: utf-8 -*-


import os
import urllib2
from BeautifulSoup import BeautifulSoup

url = raw_input('Slideshare URL : ')
html = urllib2.urlopen(url).read()

soup = BeautifulSoup(html)
title = 'hoge' #soup.title.string

images = soup.findAll('img', {'class':'slide_image'})

for image in images:
  image_url = image.get('data-full').split('?')[0]
  command = 'wget %s -P %s' % (image_url, title)
  os.system(command)
	
