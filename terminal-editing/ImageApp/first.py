#!/usr/bin/env python3
# New file created
import os
import sys
import glob

from PIL import Image
import enhancements 
import move_file_input
import file_task
from multiprocessing import Pool
from PIL import ImageFilter
from PIL import ImageOps
#move these enhancements into its own module and call it from there later nater.



class ImageApp():
    def __init__(self):
        self.files = []

    def create_images(self, infile):
 
        os.listdir()
        for infile in glob.glob("*.jpg"):
            outfile = os.path.splitext(infile)[0] + "_edited.jpg"
            if infile != outfile:
                try:
                    with Image.open(infile) as im:
                    #im1 = im.filter(ImageFilter.DETAIL)
                    #could optionally call more than one image filter function
                    #functions above are only expecting an image object and return one also.
                        im = enhancements.enhance_detail(im)
                        im = enhancements.create_thumbnail(im)
                        im.save(outfile, "JPEG", quality='maximum', subsampling=0)
                        file_task.move_file(str(outfile), 'black_white')
                        self.files.append(outfile)
                
                
                except OSError:
                    print("cannot create thumbnail for", infile)








