#!/usr/bin/env python3
#New file created
import sys
import shutil


def move_file(src, dst):
    shutil.copy(src, dst)
    print("your file {} has been moved to {}".format(src, dst))
    return 
def move_tree(src, dst):
    shutil.copytree(src, dst, symlinks=True, dirs_exist_ok=True)
    print("the directory {} has been moved to {}.".format(src, dst))
    return
    

#driving code

#move_file(src=input("enter source: \n"), dst=input("enter destination"))
#move_tree(src=input("Enter directory source: \n"), dst=input("Enter destination directory: \n"))
#should be move_to and move_from 

