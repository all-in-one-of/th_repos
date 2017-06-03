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

path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'configs/assetsCH.yml')
def get_assets_CHName(assetName):
    #print path
    dict = jarryLibs.dict2yaml(path).read()
    for type in dict.keys():
        if assetName in dict[type].keys():
            chName = dict[type][assetName]
            if chName:
                return chName
    else:
        logging.warning(u'未检测到资产中文名，可能没有录入！')
        return 'None'
        
    
if __name__ == "__main__":
    pass
