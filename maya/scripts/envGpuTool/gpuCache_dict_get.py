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
# Third-party modules

import pymel.core as pm
import maya.cmds as cmds


def gpuCache_dict_get(node,assetName,abcPath,dec):
    '''
        gpuCache dict create 
    '''
    assetTopList = node
    gpu_cache_dict = {}
    gpu_cache_dict['name'] = assetName
    gpu_cache_dict['path'] = abcPath
    meshList = []
    for mesh in pm.ls(type = 'mesh'):
        if assetTopList in mesh.longName():            
            meshList.append(mesh.getParent().longName().split('|',2)[2])            
        
    gpu_cache_dict['mesh'] = meshList
    gpu_cache_dict['dec'] = dec
    return gpu_cache_dict
        
if __name__ == "__main__":
    pass
    #node = 'TingZi_Grp'
    #assetName = 'TingZi'
    #ver = 'v001'
    #dir = 'Z:/publicExchange/jiazhihui/workSpace/tingzi/gpu/'
    #getAbcPath = gpuCache_Export(node,assetName,ver,dir)
