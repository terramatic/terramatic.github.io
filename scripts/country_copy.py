import os
import glob
import shutil

SRC_DIR = r'D:\Photos\Chile 2013\Chile_sel_big'
SRC_DIR = r'C:\xampp\htdocs\travelmatic\images\src\chile'
if not os.path.exists(SRC_DIR):
    os.makedirs(SRC_DIR)
    
## Copy selected images from src to SRC_DIR
sel_imgs = ['013', '066', '288', '272', '613', '798', '1056', '1123', '1282', '1300', '1327', '1335', '1402', '1492', '2441', '2489', '2586', '2611', '2621', '2723', '2743', '2767']
for im in sel_imgs:
	for src in glob.glob('{d}/*{a}*.JPG'.format(d=SRC_DIR, a=im)):			
		print('Copying {}'.format(src))
		shutil.copy(src, SRC_DIR)
