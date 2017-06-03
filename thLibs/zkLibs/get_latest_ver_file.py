#!/usr/bin/env python
# -*- coding: utf-8 -*-
# title       :
# description :
# author      :
# mtine       :
# version     :
# usage       :
# notes       :

# Built-in modules
import os,sys
import glob
# Third-party modules



def get_latest_ver_file(asset_dir,fileName):
    '''
        input path ,get latest version 's file
    '''
    if os.path.isdir(asset_dir):
        folders = [i for i in os.listdir(asset_dir) if i.startswith('v')]
        if folders:
            folders.sort()    
            folders = folders[::-1]
            for ver in folders:
                verPath = os.path.join(asset_dir,ver)                 
                fileList = glob.glob('%s/%s'%(verPath,fileName))
                if fileList:
                    break
            return fileList[0]
            
            
if __name__ == "__main__":
    pass

