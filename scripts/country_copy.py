import os
import glob
import shutil
import sys

if len(sys.argv) != 2:
	print 'Please input country'
	exit()
country = sys.argv[1]

ORI_DIR = r'D:\Photos\Norway 2016'
SRC_DIR = r'C:\xampp\htdocs\travelmatic\images\src\{}'.format(country)
if not os.path.exists(SRC_DIR):
    os.makedirs(SRC_DIR)

## Copy selected images from src to SRC_DIR
sel_imgs = ['1250039', '1250088', '1250099', '240692', '240732', '240753', '240760', '240778', '240803', '240821', '240867', '240947', '240957', '240962', '1250036']
for im in sel_imgs:
	if im == '': continue
	pattern = '{d}/*{a}*'.format(d=ORI_DIR, a=im)	
	for src in glob.glob(pattern):			
		print('Copying {}'.format(src))
		shutil.copy(src, SRC_DIR)
