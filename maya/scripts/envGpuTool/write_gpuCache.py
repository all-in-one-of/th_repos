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

import gpuCache_Export
import gpuCache_dict_get
#reload(gpuCache_Export)
#reload(gpuCache_dict_get)
import jarryLibs
import yaml


def write_gpuCache(assetPath,assetName,gpuFile,ymlFile,dec):
    '''
        output gpu abc file
    '''
        
    topNode = '%s_mdl_Grp'%assetName
    
    #gpu_path,gpu_Name = gpuCache_Export.gpuFilePath_Name(assetName,ver,assetPath)
    
    
    if pm.objExists(topNode):
        try:
            #gpu abc
            gpuFileFullPath = gpuCache_Export.gpuCache_Export(topNode,assetPath,gpuFile)
            if gpuFileFullPath:
                logging.info('output gpu abc:%s'%gpuFileFullPath)
                                   
            #yaml
            gpuDict = gpuCache_dict_get.gpuCache_dict_get(topNode,assetName,gpuFileFullPath,dec)
            
            ymlFileFullPath = os.path.join(assetPath,ymlFile)
            if jarryLibs.dict2yaml(ymlFileFullPath,gpuDict).write():
                logging.info('output gpu yaml:%s'%ymlFileFullPath)
                return True
        except Exception, e:
            logging.warning(e)
    else:
        logging.warning('have not this node: %s!'%topNode)


if __name__ == "__main__":
    pass
    #node = 'TingZi_Grp'
    #assetName = 'TingZi'
    #ver = 'v001'
    #dir = 'Z:/publicExchange/jiazhihui/workSpace/tingzi/gpu/'
    #getAbcPath = gpuCache_Export(node,assetName,ver,dir)
