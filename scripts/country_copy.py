import os
import glob
import shutil
import sys

if len(sys.argv) != 2:
	print 'Please input country'
	exit()
country = sys.argv[1]

ORI_DIR = r'/mnt/d/Photos/Slovakia 2019'
if not os.path.exists(ORI_DIR):
    print 'Missing directory {}'.format(ORI_DIR)
    os.makedirs(ORI_DIR)

SRC_DIR = r'/mnt/c/xampp/htdocs/travelmatic/images/src/{}'.format(country)
if not os.path.exists(SRC_DIR):
    print 'Creating directory {}'.format(country)
    os.makedirs(SRC_DIR)

## Copy selected images from src to SRC_DIR
sel_imgs = [ '00023', '0084', '00107', '00205', '00220', '00232', '00235', '00243', '00245', '00293', '00304', '00349', '00357', '00419', '00442', 'xxx', 'xx', 'xx', 'xx', 'xx'  ]
for im in sel_imgs:
	if im == '': continue
	pattern = '{d}/*{a}*'.format(d=ORI_DIR, a=im)	
	for src in glob.glob(pattern):			
		print('Copying {}'.format(src))
		print('to {}'.format(SRC_DIR))
		shutil.copy(src, SRC_DIR)
