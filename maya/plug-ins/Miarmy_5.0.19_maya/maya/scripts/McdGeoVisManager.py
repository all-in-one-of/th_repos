## +
## ===================================================================
## Copyright(C) 2010 - 2014 Basefount Software Limited.
## and/or its licensors.  All rights reserved.
##
## The coded instructions, statements, computer programs, and/or
## related material (collectively the "Data") in these files contain
## unpublished information proprietary to Basefount Technology
## Limitd. ("Basefount") and/or its licensors, which is
## protected by Chinese copyright law and by international treaties.
##
## The Data is provided for use exclusively by You. You have the right 
## to use, modify, and incorporate this Data into other products for 
## purposes authorized by the Basefount software license agreement, 
## without fee.
##
## The copyright notices in the Software and this entire statement, 
## including the above license grant, this restriction and the 
## following disclaimer, must be included in all copies of the 
## Software, in whole or in part, and all derivative works of 
## the Software, unless such copies or derivative works are solely 
## in the form of machine-executable object code generated by a 
## source language processor.
##
## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND. 
## BASEFOUNT DOES NOT MAKE AND HEREBY DISCLAIMS ANY EXPRESS OR
## IMPLIED WARRANTIES INCLUDING, BUT NOT LIMITED TO, THE WARRANTIES
## OF NON-INFRINGEMENT, MERCHANTABILITY OR FITNESS FOR A PARTICULAR 
## PURPOSE, OR ARISING FROM A COURSE OF DEALING, USAGE, OR 
## TRADE PRACTICE. IN NO EVENT WILL BASEFOUNTAIN AND/OR ITS LICENSORS 
## BE LIABLE FOR ANY LOST REVENUES, DATA, OR PROFITS, OR SPECIAL, 
## DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES, EVEN IF BASEFOUNTAIN 
## AND/OR ITS LICENSORS HAS BEEN ADVISED OF THE POSSIBILITY 
## OR PROBABILITY OF SUCH DAMAGES.
##
## ===================================================================
## -

## +
## ===================================================================
##  Module Name: McdAgentManager.py
##
##  Description:
##    For managing agent in scene, globally.
##
## ===================================================================
## -

import maya.cmds as cmds
from McdGeneral import *
from McdSimpleCmd import *
from McdGeoVisManagerGUI import *

def McdGeoVisManagerStartUpSetup():
    info = []
    
    # find terrain node, get terrain mesh:
    allGVINodes = cmds.ls(type = "McdGeoVisInfo")
    
    if MIsBlank(allGVINodes):
        return []
    
    allGVINodeNames = []
    allGeometryNames = []
    allActionNames = []
    allStartFrames = []
    allEndFrames = []
    
    # get attributes
    for i in range(len(allGVINodes)):
        allGVINodeNames.append(allGVINodes[i]);
        
        df = cmds.getAttr(allGVINodes[i] + ".geometryName")
        allGeometryNames.append(df)
        sf = cmds.getAttr(allGVINodes[i] + ".actionName")
        allActionNames.append(sf)
        rt = cmds.getAttr(allGVINodes[i] + ".startFrame")
        allStartFrames.append(rt)
        ia = cmds.getAttr(allGVINodes[i] + ".endFrame")
        allEndFrames.append(ia)

    info.append(allGVINodeNames)
    info.append(allGeometryNames)
    info.append(allActionNames)
    info.append(allStartFrames)
    info.append(allEndFrames)
            
    return info

def McdAddGeoVisCondition():
    cmds.createNode("McdGeoVisInfo")
    McdRefreshGeoVisManager()

def deleteGVINode(i):
    stri = str(i)
    toBeDel = cmds.textField("GVINode_tf" + stri, q = True, tx = True)
    cmds.delete(toBeDel)
    McdRefreshGeoVisManager()

def changeGVIGN(index):
    stri = str(index)
    nodeName = cmds.textField("GVINode_tf" + stri, q = True, tx = True)
    value = cmds.textField("geoName_tf" + stri, q = True, tx = True)
    
    cmds.setAttr(nodeName + ".geometryName", value, type = "string")
    
def changeGVIAN(index):
    stri = str(index)
    nodeName = cmds.textField("GVINode_tf" + stri, q = True, tx = True)
    value = cmds.textField("actionName_tf" + stri, q = True, tx = True)
    
    cmds.setAttr(nodeName + ".actionName", value, type = "string")
    
def changeGVISF(index):
    stri = str(index)
    nodeName = cmds.textField("GVINode_tf" + stri, q = True, tx = True)
    value = cmds.intField("startFrame_ff" + stri, q = True, v = True)
    
    cmds.setAttr(nodeName + ".startFrame", value)

def changeGVIEF(index):
    stri = str(index)
    nodeName = cmds.textField("GVINode_tf" + stri, q = True, tx = True)
    value = cmds.intField("endFrame_ff" + stri, q = True, v = True)
    
    cmds.setAttr(nodeName + ".endFrame", value)














    
    
    