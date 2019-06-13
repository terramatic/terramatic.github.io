import os
from PIL import Image

FULL_DIR = r'C:\xampp\htdocs\images\fulls\morroco'
THUMBS_DIR = r'C:\xampp\htdocs\images\thumbs\morroco'

## Create thumbnails
size = [256, 256]
for f in os.listdir(FULL_DIR):
	infile = os.path.join(FULL_DIR, f)
	outfile = os.path.join(THUMBS_DIR, f)
	print('thumbnail {} to {}'.format(infile, outfile))
	im = Image.open(infile)
	im.thumbnail(size)
	im.save(outfile, "JPEG")