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
# Third-party modules
import json


class dict2json(object):
    def __init__(self,path,dict = {}):
        self._path = path
        self._dict = dict
    #写入json文件
    def write(self):
        try:
            f = open(self._path, 'w')
            f.write(json.dumps(self._dict,indent=2))
            f.close()
            return True
        except:
            logging.error(u'You have no rights!')
            return False    
        
    #读取json文件
    def read(self):
        if os.path.isfile(self._path):
            f = open(self._path, 'r')
            data = json.loads(f.read())
            f.close()
            return data
        else:
            return False
            
            
if __name__ == "__main__":
    pass