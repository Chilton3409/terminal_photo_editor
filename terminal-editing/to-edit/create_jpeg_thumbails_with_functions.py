#!/usr/bin/env python3
# New file created
import os
import sys
import glob

from PIL import Image
from file_task import move_file
from multiprocessing import Pool
from PIL import ImageFilter
from PIL import ImageOps
#move these enhancements into its own module and call it from there later nater.
def enhance_detail(im):
    im = im.filter(ImageFilter.DETAIL)
    return im

def enhance_contour(im):
    im = im.filter(ImageFilter.CONTOUR)
    return im 

def enhance_3dColorLut(im):
    #need to look up size and table parameters that go with this function 
    im = im.filter(ImageFilter.Color3DLUT)
    return im 

def enhance_edges(im):
    im = im.filter(ImageFilter.EDGE_ENHANCE)
    return im 

def enhance_edges_more(im):
    im = im.filter(ImageFilter.EDGE_ENHANCE_MORE)
    return im

def create_thumbnail(im):
    size = (600, 400)
    im = im.thumbnail(size)
    return im

def create_images(infile):
    """
    to use this, first create a dir called thumbnails to store your photos
    open the terminal and run the script with the path to the folder you want edit as a parameter
    like ./file.py ./path-to-folder 

    """
    os.listdir()
    for infile in glob.glob("*.JPG"):
     
        outfile = os.path.splitext(infile)[0] + "_edited.jpg"
        if infile != outfile:
            try:
                with Image.open(infile) as im:
                    #im1 = im.filter(ImageFilter.DETAIL)
                    #could optionally call more than one image filter function
                    #functions above are only expecting an image object and return one also.
                    
                    im = enhance_detail(im)
                    im = enhance_edges_more(im)
                    create_thumbnail(im)
               
                    im.save(outfile, "JPEG", quality='maximum', subsampling=0)
                    print("file {} created.".format(infile))
                    move_file(str(outfile), 'black_white')
                    

            except OSError:
                print("cannot create thumbnail for", infile)

if __name__ == "__main__":
    with Pool(4) as p:
        p.map(create_images, [str(sys.argv[1])])


    #create_thumbnails(str(sys.argv[1]))

    
