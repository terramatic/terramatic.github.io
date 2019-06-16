import os
import sys
from PIL import Image

if len(sys.argv) != 2:
	print 'Please input country'
	exit()
country = sys.argv[1]
SRC_DIR = r'C:\xampp\htdocs\travelmatic\images\src\{}'.format(country)
FULL_DIR = r'C:\xampp\htdocs\travelmatic\images\fulls\{}'.format(country)
THUMBS_DIR = r'C:\xampp\htdocs\travelmatic\images\thumbs\{}'.format(country)

if not os.path.exists(FULL_DIR):
    os.makedirs(FULL_DIR)
if not os.path.exists(THUMBS_DIR):
    os.makedirs(THUMBS_DIR)

## Create thumbnails
xsW = 256
xlW = 1920

print SRC_DIR
for f in os.listdir(SRC_DIR):
	# Filenames
	outfileXL = os.path.join(FULL_DIR, f)
	outfileXS = os.path.join(THUMBS_DIR, f)
	
	# Source
	infile = os.path.join(SRC_DIR, f)
	im = Image.open(infile)
	wpercent = (xsW/float(im.size[0]))
	xsH = int((float(im.size[1])*float(wpercent)))
	wpercent = (xlW/float(im.size[0]))
	xlH = int((float(im.size[1])*float(wpercent)))

	# XS
	print('thumbnail {} to {}'.format(infile, outfileXS))
	img = im.resize((xsW, xsH), Image.ANTIALIAS)
	img.save(outfileXS, "JPEG")

	# XL
	print('thumbnail {} to {}'.format(infile, outfileXL))	
	img = im.resize((xlW, xlH), Image.ANTIALIAS)
	img.save(outfileXL, "JPEG")	