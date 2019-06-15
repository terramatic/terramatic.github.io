import os
import glob
import shutil

SRC_DIR = r'C:\Users\sala\OneDrive - Stichting Deltares\Desktop\Azerbaijan'
FULL_DIR = r'C:\xampp\htdocs\travelmatic\images\src\azerbaijan'

## Copy selected images from src to FULL_DIR
sel_imgs = ['1562', '1670', '1677', '1688', '1712', '1832', '1879', '1920', '1947', '2003', '2023', '2071', '2103', '2388', '2441', '2489', '2586', '2611', '2621', '2723', '2743', '2767']
for im in sel_imgs:
	for src in glob.glob('{d}/*{a}*.JPG'.format(d=SRC_DIR, a=im)):			
		print('Copying {}'.format(src))
		shutil.copy(src, FULL_DIR)
