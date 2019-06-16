import os
import glob
import shutil
import sys

if len(sys.argv) != 2:
	print 'Please input country'
	exit()
country = sys.argv[1]

ORI_DIR = r'D:\Photos\Hyderabad 2017'
SRC_DIR = r'C:\xampp\htdocs\travelmatic\images\src\{}'.format(country)
if not os.path.exists(SRC_DIR):
    os.makedirs(SRC_DIR)

## Copy selected images from src to SRC_DIR
sel_imgs = ['P1250922', 'P1250924', 'P1250958', 'P1250984', '126085', '1260165', '1260172', '1260195', '1260217', '1260218', '', '', '', '', '', '', '', '', '', '', '', '']
for im in sel_imgs:
	if im == '': continue
	pattern = '{d}/*{a}*'.format(d=ORI_DIR, a=im)	
	for src in glob.glob(pattern):			
		print('Copying {}'.format(src))
		shutil.copy(src, SRC_DIR)
