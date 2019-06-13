import os
import glob
import shutil

#SRC_DIR = r'C:\Users\sala\OneDrive - Stichting Deltares\Desktop\Morroco 2019'
#FULL_DIR = r'C:\xampp\htdocs\images\fulls\morroco'

## Copy selected images from src to FULL_DIR
sel_imgs = ['076', '082', '127', '128', '137', '147', '256', '191', '9151', '233', '252', '270', '303', '439', '484', '495', '618', '523', '642', '698', '719', '750', '764', '878', '886', '']
for im in sel_imgs:
	for src in glob.glob('{d}/*{a}*.JPG'.format(d=SRC_DIR, a=im)):			
		print('Copying {}'.format(src))
		shutil.copy(src, FULL_DIR)
