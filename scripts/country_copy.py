import os
import glob
import shutil

ORI_DIR = r'D:\Photos\Switzerland 2017'
SRC_DIR = r'C:\xampp\htdocs\travelmatic\images\src\switzerland'
if not os.path.exists(SRC_DIR):
    os.makedirs(SRC_DIR)

## Copy selected images from src to SRC_DIR
sel_imgs = ['0215', '504', '577', '583', '615', '676', '685', '691', '700', '775', '', '', '', '', '', '', '', '', '', '', '', '']
for im in sel_imgs:
	if im == '': continue
	pattern = '{d}/*{a}*'.format(d=ORI_DIR, a=im)	
	for src in glob.glob(pattern):			
		print('Copying {}'.format(src))
		shutil.copy(src, SRC_DIR)
