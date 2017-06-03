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



def get_ver_file_dictList(asset_dir,fileName):
    '''
        input path ,get latest version 's file
    '''
    verDict = {}
    if os.path.isdir(asset_dir):
        folders = [i for i in os.listdir(asset_dir) if i.startswith('v')]
        if folders:
            folders.sort()    
            folders = folders[::-1]
            for ver in folders:
                verPath = os.path.join(asset_dir,ver)                 
                fileList = glob.glob('%s/%s'%(verPath,fileName))
                if fileList:
                    #break
                    verDict[ver] = fileList[0]
            return verDict
            
            
if __name__ == "__main__":
    pass
    #ASSETS_ENV_PATH = 'Z:\ZK_Project\Assets\Publish\Environment'
    #asset = 'PEDanFengDoor'
    #setp = 'gpu'
    #assetDir = os.path.join(ASSETS_ENV_PATH,asset,setp)
    #fileName = '%s_%s_*.yml'%(asset,setp)
    
    #result = get_ver_file_dictList(assetDir,fileName)
    #print result