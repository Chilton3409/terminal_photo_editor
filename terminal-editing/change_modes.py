#!/usr/bin/env python3
#New file created
import os
import sys
import glob
from PIL import Image
from multiprocessing import Pool
path = os.getcwd()


if os.path.isdir(path):

    #os.mkdir("thumbnails")
    for infile in glob.glob("*.jpg"):
        im = Image.open(infile)