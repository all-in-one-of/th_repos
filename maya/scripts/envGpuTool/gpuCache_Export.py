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

import pymel.core as pm
import maya.cmds as cmds

def gpuFilePath_Name(assetName,ver,dir):
    file_Name = '%s_gpu_%s'%(assetName,ver)
    file_path = os.path.join(dir,'gpu',ver)
    return file_path,file_Name
    
def gpuCache_Export(node,file_path,file_Name):
    '''
        publish this gpuCache file    
    '''
    #exportFile_Name = '%s_gpu_%s'%(assetName,ver)
    #file_path,file_Name = gpuFilePath_Name(assetName,ver,dir)
    #dir = os.path.join(dir,ver)
    
    
    try:
        output = pm.gpuCache(node,
                    startTime=1, 
                    endTime=1,
                    #optimize=True, 
                    #optimizationThreshold=100,
                    directory = file_path,
                    fileName = file_Name
                    )
        return output[0]
    except Exception, e:
        logging.warning(e)
        
if __name__ == "__main__":
    pass
    #node = 'TingZi_Grp'
    #assetName = 'TingZi'
    #ver = 'v001'
    #dir = 'Z:/publicExchange/jiazhihui/workSpace/tingzi/gpu/'
    #getAbcPath = gpuCache_Export(node,assetName,ver,dir)
