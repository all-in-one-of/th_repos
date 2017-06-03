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
import re
# Third-party modules



 
class modifyFile(object):
    '''
        修改文件内容，修改ma文件中的垃圾信息，降版本2015 to 2014
    
    '''
    def __init__(self,path):
        self._path = path
    def modify(self,path,sstr,rstr):    
        try:        
            lines=open(path,'r').readlines()
            flen=len(lines)-1
            
            for i in range(flen):            
                get =  re.findall(sstr,lines[i])
                if get:
                    if get[0] in lines[i]:
                        new = lines[i].replace(get[0],rstr)
                        #print len(new)
                        if len(new) == 1:
                            lines[i]= ''
                        else:
                            lines[i]= new

            open(path,'w').writelines(lines)
            print 'modify ma done!'
        except Exception,e:
            print e
        
    def killRubbish(self):
        self.modify(self._path,'(requires "\w+.*)$[^0-9]','')
        
    def version(self):
        self.modify(self._path,'2015";','2014";')
            
if __name__ == "__main__":
    pass

