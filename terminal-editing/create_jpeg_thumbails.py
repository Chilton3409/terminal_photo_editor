#!/usr/bin/env python3
#New file created
import os, sys
import glob
from PIL import Image
from file_task import move_file



size = (1280, 720)


for infile in glob.glob("*.jpg"):
    outfile = os.path.splitext(infile)[0] + "_thumbnail.jpg"
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                im.thumbnail(size)
                im.save(outfile, "JPEG", quality=95, subsampling=0)
                print("file {} created.".format(infile))
                move_file(str(outfile), 'thumbnails')
                
        except OSError:
            print("cannot create thumbnail for", infile)

#it is important to note that the library doesnt decode the raster unlessi t has too


