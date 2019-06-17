import os
import glob
import shutil
import sys

if len(sys.argv) != 2:
	print 'Please input country'
	exit()
country = sys.argv[1]

ORI_DIR = r'D:\Photos\Kuwait_2018'
SRC_DIR = r'C:\xampp\htdocs\travelmatic\images\src\{}'.format(country)
if not os.path.exists(SRC_DIR):
    os.makedirs(SRC_DIR)

## Copy selected images from src to SRC_DIR
sel_imgs = ['2748', '2752', '2759', '2795', '2842', '2859', '2890', '2899', '2914', '2943', '2998', '2995', '', '', '', '', '', '', '', '', '', '']
for im in sel_imgs:
	if im == '': continue
	pattern = '{d}/*{a}*'.format(d=ORI_DIR, a=im)	
	for src in glob.glob(pattern):			
		print('Copying {}'.format(src))
		shutil.copy(src, SRC_DIR)
