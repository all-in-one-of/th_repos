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
import os
import glob
import re
import logging
# Third-party modules
try:
    import pymel.core as pm
except:
    pass

def getAssetInfoFromFile(sceneName = ''):
    sceneName = pm.sceneName()
    if not sceneName:
        logging.warning('have not file')
        return
    dirname = os.path.dirname(sceneName)
    basename = os.path.basename(sceneName)
    floderAssetName = dirname.split('/')[5]
    fileAssetName = basename.split('_')[0]
    floderVersion = re.match(r".*(v\d{3}).*", dirname).group(1)
    fileVersion = re.match(r".*_(v\d{3}).*", basename).group(1)
    
    

    if fileAssetName == floderAssetName:
        assetName = fileAssetName
    else:
        logging.warning(u'文件名起错了吧')
    if fileVersion == floderVersion:
        version = fileVersion
    else:
        logging.warning(u'文件名上的版本号和文件夹不统一')
        
    path = re.findall(r'\w+.*%s'%assetName, dirname)[0]
    return path,assetName,version
    
if __name__ == "__main__":
    pass
