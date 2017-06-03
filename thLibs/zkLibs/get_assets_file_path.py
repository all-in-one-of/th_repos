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


import jarryLibs

path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'configs/zkConfig.yml')
def get_assets_file_path(assetName,state,step,ver = None,ext = None):
    #print path
    dict = jarryLibs.dict2yaml(path).read()
    
    projPath = dict['projectPath']
    assets = dict['assets']
    filePathFormatList = dict['filePathFormat']
    if state not in dict['state']:
        logging.warning(u'Not exists state: %s'%state)
        return 
    for type in dict['type']:        
        assetNamePath = dict['assetName'].format(projectPath = projPath,assets = assets,state = state,type = type)
        if assetName in os.listdir(assetNamePath):
                
            for stepInfo in filePathFormatList:
                if step in stepInfo.keys():
                    filePathFormat = stepInfo[step]['path']
                    fileFormat = stepInfo[step]['file']
                    try:
                        result_path = filePathFormat.format(projectPath = projPath,
                                                    assets = assets,
                                                    state = state,
                                                    type = type,
                                                    step = step,
                                                    id = assetName,
                                                    ver = ver,
                                                    ext = ext)
                        result_file = fileFormat.format(projectPath = projPath,
                                                    assets = assets,
                                                    state = state,
                                                    type = type,
                                                    step = step,
                                                    id = assetName,
                                                    ver = ver,ext= ext)
                        return result_path,result_file
                    except:
                        logging.warning(u'未检测到项目信息，可能没有录入！')
                        return 
    
    logging.warning(u'未检测到资产名称，可能没有录入！')  
if __name__ == "__main__":
    pass
