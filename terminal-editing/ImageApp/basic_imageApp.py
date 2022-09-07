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
        self.old_files = []

    def unpack(self):
        dst=input("Where would you like to store these files.")
        for file in self.files:
            file_task.move_file(src=str(file), dst=dst)
            print("The file {} has been moved.".format(file))

    def create_images(self, infile):
        infile = os.listdir()
        for infile in glob.glob("*.jpg"):
            outfile = os.path.splitext(infile)[0] + "_edited.jpg"
          
            if infile != outfile:
                try:
                    with Image.open(infile) as im:
                    #im1 = im.filter(ImageFilter.DETAIL)
                    #could optionally call more than one image filter function
                    #functions above are only expecting an image object and return one also.
                    
                        im = enhancements.enhance_detail(im)
                 
                        #enhancements.create_thumbnail(im)
               
                        im.save(outfile, "JPEG", quality='maximum', subsampling=0,)
                        self.files.append(outfile)
                        self.old_files.append(infile)
                        #file_task.move_file(str(outfile), 'black_white')

            #print(infile)
                except OSError:
                    print("cannot create thumbnail for", infile)

                
                print(self.files)
        

if __name__=='__main__':
   x = ImageApp()
   x.create_images(infile=input("Enter directory to get a list of its files: \n"))
   x.unpack()

 




