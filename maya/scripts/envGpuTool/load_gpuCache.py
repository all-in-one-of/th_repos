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
import logging
import pymel.core as pm
import maya.cmds as cmds

import jarryLibs

def create_hierarchy_xform(longName,topNode=''):
    '''
        input longName ,and create hierarchy group ,output node
        
    '''
    if not pm.objExists(topNode+'|'+longName):
        newName = topNode
        hierarchy = longName.split('|')
        for i in hierarchy:
            newName += '|'+i
            
            if not pm.objExists(newName):
                try:   
                    parent = newName[::-1].replace( ('|'+i)[::-1],'',1) [::-1]
                     
                    output = pm.createNode('transform',n = i,p=parent)                    
                except:
                    return False
    return pm.PyNode(topNode+'|'+longName)
                


def create_gpu_node(xformNode,gpuPath,geoPath):
    '''
        create gpu node with shapeNode ,edit abc path,and edit geo path
    '''
    gpuNodeName = xformNode.split('|')[-1]+'Shape'
    geoPath = '|%s'%geoPath
    if not pm.objExists(xformNode + '|'+gpuNodeName):
        gpuNode = pm.createNode('gpuCache',n = gpuNodeName,p=xformNode)
        gpuNode.cacheFileName.set(gpuPath)
        gpuNode.cacheGeomPath.set(geoPath)
        #gpuNode.cmp.setAttr(l=1)
        
        #setAttr -l true { "wapian_011_gpuShape.cmp" };
        return gpuNode
        
    #elif pm.objExists(gpuNodeName):
    #    gpuNode = pm.PyNode(xformNode + '|'+gpuNodeName)
    #    gpuNode.cacheFileName.set(gpuPath)
    #    gpuNode.cacheGeomPath.set(geoPath)
    #    return gpuNode

    
    
def load_gpuCache_dict(gpuDict_yamlPath):
    '''
        load this gpuCache with group    
    '''
    dict = jarryLibs.dict2yaml(gpuDict_yamlPath).read()
    gpuToNode = 'Environment_Grp'
    if not pm.objExists(gpuToNode):
        gpuToNode = pm.createNode('transform',n = gpuToNode)
    else:
        gpuToNode = pm.PyNode(gpuToNode)
    gpu_cache_dict = dict
    topNode = gpu_cache_dict[u'name'] + '_gpu_grp'
    gpuPath = gpu_cache_dict[u'path']
    longNameList = gpu_cache_dict['mesh']
    
    if not pm.objExists(topNode):
        topNode = pm.createNode('transform',n = topNode)
        #gpuToNode | topNode 
        try:
            pm.parent(topNode,gpuToNode)
        except:
            pass
    else:
        topNode = pm.PyNode(topNode)
    size = len(longNameList)
    for x,longName in enumerate(longNameList):
        geoPath = longName
        longName = longName + '_gpu'
        
        xformNode = create_hierarchy_xform(longName,topNode)
        #get gpu parent node 
        create_gpu_node(xformNode,gpuPath,geoPath)
        
        pm.xform(xformNode.name(),centerPivots=True)
        
        n = float(x)/len(longNameList)*100

        yield n

        
def load_gpuCache_single(gpuDict_yamlPath):
    dict = jarryLibs.dict2yaml(gpuDict_yamlPath).read()
    gpuToNode = 'Environment_Grp'
    if not pm.objExists(gpuToNode):
        gpuToNode = pm.createNode('transform',n = gpuToNode)
    else:
        gpuToNode = pm.PyNode(gpuToNode)
    gpu_cache_dict = dict
    topNode = gpu_cache_dict[u'name'] + '_gpu'
    gpuPath = gpu_cache_dict[u'path']
    
    if not pm.objExists(topNode):
        topNode = pm.createNode('transform',n = topNode)        
        #gpuToNode | topNode 
        create_gpu_node(topNode,gpuPath,'')   
        try:
            pm.parent(topNode,gpuToNode)
        except:
            pass        
        return True
    else:
        logging.info(u'exists gpuCache :%s'%gpu_cache_dict[u'name'])                
        return False
        
'''
def load_single_gpuCache_doIt(gpuDict_yamlPath):    
    try:
        getGpuYaml = jarryLibs.dict2yaml(gpuDict_yamlPath).read()
        if load_gpuCache_single(getGpuYaml):
            return True
        else:
            return None
    except:
        return False      
        
        
def load_gpuCache_doIt(gpuDict_yamlPath):    
    try:
        getGpuYaml = jarryLibs.dict2yaml(gpuDict_yamlPath).read()
        load_gpuCache_dict(getGpuYaml)
        return True
    except:
        return False
        
        '''

if __name__ == "__main__":
    pass
    #node = 'TingZi_Grp'
    #assetName = 'TingZi'
    #ver = 'v001'
    #dir = 'Z:/publicExchange/jiazhihui/workSpace/tingzi/gpu/'
    #getAbcPath = gpuCache_Export(node,assetName,ver,dir)
