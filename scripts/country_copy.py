import os
import glob
import shutil
import sys

if len(sys.argv) != 2:
	print 'Please input country'
	exit()
country = sys.argv[1]

ORI_DIR = r'D:\Photos\NYC2017'
SRC_DIR = r'C:\xampp\htdocs\travelmatic\images\src\{}'.format(country)
if not os.path.exists(SRC_DIR):
    os.makedirs(SRC_DIR)

## Copy selected images from src to SRC_DIR
sel_imgs = [ '60334', '60345', '60556', '60668', '60756', '60367', '60525', '2458', '2448', '2492', '2502', 'xx', 'xxxx', 'xxx', 'xx', 'xxx', 'xx', 'xx', 'xx', 'xx'  ]
for im in sel_imgs:
	if im == '': continue
	pattern = '{d}/*{a}*'.format(d=ORI_DIR, a=im)	
	for src in glob.glob(pattern):			
		print('Copying {}'.format(src))
		shutil.copy(src, SRC_DIR)
