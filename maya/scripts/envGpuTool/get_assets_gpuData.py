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
import logging
# Third-party modules

import zkLibs


ASSETS_ENV_PATH = 'Z:\ZK_Project\Assets\Publish\Environment'
STEP = 'gpu'

def get_gpu_inscene(assetName):
    try:
        import pymel.core as pm
        
        getTopNode = pm.ls('Environment_Grp')
        if not getTopNode:            
            #logging.warning('Have not top node:Environment_Grp! ')
            return
           
        getAssetGpu = pm.ls('%s_gpu'%assetName)        
        getAssetGpuGrp = pm.ls('%s_gpu_grp'%assetName)
        if not getAssetGpu and not getAssetGpuGrp:
            #logging.warning('Have not top node:Environment_Grp! ')
            return         
        elif getAssetGpu or getAssetGpuGrp:
            return getAssetGpu or getAssetGpuGrp
    except:
        logging.error('error')
        pass
        
def get_assets_gpuData():
    gpuFileDictList = {}
    yamlFileList = []
    for asset_floder in os.listdir(ASSETS_ENV_PATH):
        gpuFileDict = {}
        
        asset_dir = os.path.join(ASSETS_ENV_PATH,asset_floder,STEP)          
        get_ver_file = zkLibs.get_ver_file_dictList(asset_dir,'%s_%s_*.yml'%(asset_floder,STEP))
        
        if os.path.isdir(asset_dir) and get_ver_file:
            gpuFileDict['assetname'] = asset_floder
            gpuFileDict['assetCHName'] = zkLibs.get_assets_CHName(asset_floder)
            #gpuFileDict['yaml'] = get_gpu_yaml_file
            gpuFileDict['version'] = get_ver_file #zkLibs.getAssetInfoFromFile(get_gpu_yaml_file.replace('\\','/'))[2]
            
            preivewPath = '%s/%s.jpg'%(os.path.join(ASSETS_ENV_PATH,asset_floder),asset_floder)
            previewFileList = glob.glob(preivewPath)
            if previewFileList:
                gpuFileDict['preview'] = previewFileList[0]
            else:
                gpuFileDict['preview'] = ''
            
            inscene = get_gpu_inscene(asset_floder)
            if inscene:
                gpuFileDict['inscene'] = 'yes'
            else:
                gpuFileDict['inscene'] = ''
            gpuFileDictList[asset_floder] = gpuFileDict
    return gpuFileDictList


if __name__ == "__main__":
    pass

