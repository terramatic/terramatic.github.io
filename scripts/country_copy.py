import os
import glob
import shutil
import sys

if len(sys.argv) != 2:
	print 'Please input country'
	exit()
country = sys.argv[1]

ORI_DIR = r'D:\Photos\Indonesia 2017'
SRC_DIR = r'C:\xampp\htdocs\travelmatic\images\src\{}'.format(country)
if not os.path.exists(SRC_DIR):
    os.makedirs(SRC_DIR)

## Copy selected images from src to SRC_DIR
sel_imgs = [ '0829', '70010', '70026', '70052', '70053', '70125', '70221', '70224', '70303', '70353', '70390', '70674', '70690', '70764', '70767', '8068', '80103', '80238', '80470', '80583'  ]
for im in sel_imgs:
	if im == '': continue
	pattern = '{d}/*{a}*'.format(d=ORI_DIR, a=im)	
	for src in glob.glob(pattern):			
		print('Copying {}'.format(src))
		shutil.copy(src, SRC_DIR)
