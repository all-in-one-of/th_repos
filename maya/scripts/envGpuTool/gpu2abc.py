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
# Third-party modules
import logging
import pymel.core as pm



import load_gpuCache as lg


def gpu_conver_mesh():
    gpuSLList = pm.ls(sl=1)
        
    if not gpuSLList:
        logging.info(u'请选中gpu节点!')
        return
        
    for gpuSL in gpuSLList:
        if gpuSL.getShape().type() != 'gpuCache':
            logging.info(u'请选中gpu节点!当前选中的%s这个不是'%gpuSL)
            return             
        
        gpuPath = gpuSL.cacheFileName.get()
        geoPath = gpuSL.cacheGeomPath.get()
        geoPath_remove_mesh = geoPath.replace('|'+geoPath.split('|')[-1],'')
        
        assetName = os.path.basename(gpuPath).split('_')[0]
    
        gpuToNode = 'Environment_Grp'
        if not pm.objExists(gpuToNode):
            gpuToNode = pm.createNode('transform',n = gpuToNode)
        else:
            gpuToNode = pm.PyNode(gpuToNode)
            
        abcTopNode = '%s_abc_grp'%assetName
        mdlGrp = '%s_mdl_Grp'%assetName
    
        if not pm.objExists(abcTopNode):
            topNode = pm.createNode('transform',n = abcTopNode)
            try:
                pm.parent(abcTopNode,gpuToNode)
            except:
                pass
        else:
            abcTopNode = pm.PyNode(abcTopNode)
            
        parentNode = lg.create_hierarchy_xform(abcTopNode+geoPath_remove_mesh,gpuToNode)
    
        abcMesh_iName = geoPath.replace('|','/')
        
        abcMesh_oName ='|'+ mdlGrp + abcMesh_iName.replace('/','|')
        
        abcMesh_Name = abcMesh_iName.split('/')[-1]+'_abc'
        print abcMesh_Name
        if not pm.objExists(abcMesh_Name):        
            pm.AbcImport(gpuPath,mode = "import",ft = abcMesh_iName,rcs= 1,rpr = '%s'%parentNode)
        
            meshNode = un_down_Hierarchy_Group(parentNode,abcMesh_oName)
    
            gpuSL.hide()
        else:
            logging.info(u'已经存在:%s,若还想获取该模型，可以将之前转换的模型改下名字！'%abcMesh_Name)
            
def un_down_Hierarchy_Group(up,down):
    for i in down.split('|')[1:-1]:
        if i:
            to_sl = up + '|' + i
            if pm.objExists(to_sl):
                pm.select(to_sl,r=1)
                pm.mel.Ungroup()
    ouput = pm.ls(sl=1)[0].rename(down.split('|')[-1]+'_abc')
    return ouput
    
if __name__ == "__main__":
    pass

