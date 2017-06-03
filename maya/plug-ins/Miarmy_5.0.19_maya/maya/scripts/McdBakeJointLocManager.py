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
##  Module Name: Bake joint locator manager
##
##  Description:
##    For managing Particle in scene, globally.
##
## ===================================================================
## -

import maya.cmds as cmds
import maya.mel as mel
from McdGeneral import *
from McdSimpleCmd import *
from McdBakeJointLocManagerGUI import *

def McdBakeRecInit():
    info = []
    
    globalNode = McdGetMcdGlobalNode()
    
    nbRec = cmds.getAttr(globalNode + ".bkRecNum")
    
    if nbRec == 0:
        return info
    
    for i in range(nbRec):
        stri = str(i)
        
        bn = cmds.getAttr(globalNode + ".bkJoint[" + stri + "]")
        if bn == None:
            info.append("")
        else:
            info.append(bn)
        an = cmds.getAttr(globalNode + ".bkAction[" + stri + "]")
        if an == None:
            info.append("")
        else:
            info.append(an)
        sf = cmds.getAttr(globalNode + ".bkSFrame[" + stri + "]")
        info.append(sf)
        ef = cmds.getAttr(globalNode + ".bkEFrame[" + stri + "]")
        info.append(ef)
        
        sx = cmds.getAttr(globalNode + ".bkScaleX[" + stri + "]")
        info.append(sx)
        
        
    return info



def McdExpandBakeRec():
    globalNode = McdGetMcdGlobalNode()
    
    nbRec = cmds.getAttr(globalNode + ".bkRecNum")
    nbRec += 1
    cmds.setAttr(globalNode + ".bkRecNum", nbRec)
        
        
        
def McdDeleteBakeRec():
    globalNode = McdGetMcdGlobalNode()
    
    nbRec = cmds.getAttr(globalNode + ".bkRecNum")
    nbRec -= 1
    cmds.setAttr(globalNode + ".bkRecNum", nbRec)
    
    

def McdSelectEmitter(index):
    stri = str(index)
    meshName = cmds.textField("emitterShape_tf" + stri, q = True, tx = True)
    try:
        cmds.select(meshName)
    except:
        pass

# ##########################################################################

def changeBKManagerBN(index, globalNode):
    stri = str(index)

    value = cmds.textField("boneName_bktf" + stri, q = True, tx = True)
    
    cmds.setAttr(globalNode + ".bkJoint[" + stri + "]", value, type = "string")
    

def changeBKManagerAN(index, globalNode):
    stri = str(index)

    value = cmds.textField("actionName_bktf" + stri, q = True, tx = True)
    
    cmds.setAttr(globalNode + ".bkAction[" + stri + "]", value, type = "string")
    

def changeBKManagerSF(index, globalNode):
    stri = str(index)

    value = cmds.intField("startFrame_bkff" + stri, q = True, v = True)
    
    cmds.setAttr(globalNode + ".bkSFrame[" + stri + "]", value)
    
    
def changeBKManagerEF(index, globalNode):
    stri = str(index)
    value = cmds.intField("endFrame_bkff" + stri, q = True, v = True)
    
    cmds.setAttr(globalNode + ".bkEFrame[" + stri + "]", value)
    
def changeBKManagerSX(index, globalNode):
    stri = str(index)
    value = cmds.floatField("scaleX_bkff" + stri, q = True, v = True)
    
    cmds.setAttr(globalNode + ".bkScaleX[" + stri + "]", value)
    
def changeBKManagerSD(globalNode):
    value = cmds.floatField("scaleD_bk", q = True, v = True)
    
    cmds.setAttr(globalNode + ".bkScaleD", value)
    
def bakeJointActionInfoToLocator():

    # pre check:
    allAgents = cmds.ls(type = "McdAgent")
    if allAgents == [] or allAgents == None:
        cmds.confirmDialog(t = "Auto abort", m = "There is no agent in scene for baking locators.")
        return

    # pre check:
    globalNode = McdGetMcdGlobalNode()
    enCache = cmds.getAttr(globalNode + ".enableCache")
    if enCache:
        cmds.confirmDialog(t = "Error", m = "It is only able to bake locators when simulation, non-cached scene.")
        return
    
    

    startFrame = cmds.playbackOptions(q =True, min = True)
    endFrame = cmds.playbackOptions(q =True, max = True)
    
    stat = cmds.confirmDialog(t = "Bake Locators", m = "The agent cache information:\n" + \
                                            "Start Frame " + str(startFrame) + "\n" + \
                                            "End Frame: " + str(endFrame) + "\n" + \
                                            "Before baking, we suggest you save your scene", \
                                            b = ["Continue", "Cancel"])
    if stat == "Cancel":
        return

    brainNode = mel.eval("McdSimpleCommand -execute 3")
    solverFrame = cmds.getAttr(brainNode + ".startTime")
    solverFrame -= 1
    if solverFrame > startFrame:
        solverFrame = startFrame
    
    amount = 0
    counter = 0
    totalCount = endFrame - startFrame
    cmds.progressWindow( title = "Caching:", progress = 0, \
                      min = 0, max = 100, \
                      status = "caching", isInterruptable = True )
    
    autoKeyState = cmds.autoKeyframe( q = True, state = True)
    cmds.autoKeyframe( e = True, state = False)
    
    # from solverFrame to endFrame:
    while(solverFrame <= endFrame):
        
        cmds.currentTime(solverFrame)
        
        if solverFrame >= startFrame:
            # deal with batch cache
            bakeJointActionInfoToLocatorWrapper()
            
        solverFrame += 1
        
        ## progress operation: ////////////////////////////////////////////////
        if cmds.progressWindow( query = True, isCancelled = True ):
            cmds.autoKeyframe( e = True, state = autoKeyState)
            break
        
        counter += 1
        amount = float(counter) / float(totalCount) * 100.0
        cmds.progressWindow( edit = True, progress = amount)
    cmds.progressWindow(endProgress=1)
    
    cmds.autoKeyframe( e = True, state = autoKeyState)
    
    locRoot = cmds.ls("McdJALocRoot")
    if MIsBlank(locRoot):
        cmds.spaceLocator(n = "McdJALocRoot")
        
    allLoc = cmds.ls("McdJALoc_*", type = "transform")
    cmds.parent(allLoc, "McdJALocRoot")
        

def bakeJointActionInfoToLocatorWrapper():
    
    globalNode = McdGetMcdGlobalNode()
    bkScaleDef = cmds.getAttr(globalNode + ".bkScaleD")
    
    melCmd = "McdSimpleCommand -exe 12;"
    locInfo = mel.eval(melCmd)
    
    try:
        nbLoc = len(locInfo) / 8
    except:
        cmds.progressWindow(endProgress=1)
        raise Exception("return array is blank (None)")
    
    for i in range(nbLoc):
        
        scaleX = locInfo[i*8+7]
        
        stri = str(i)
        locName = "McdJALoc_" + stri
        try:
            cmds.setAttr(locName + ".tx", locInfo[i*8])
            cmds.setAttr(locName + ".ty", locInfo[i*8+1])
            cmds.setAttr(locName + ".tz", locInfo[i*8+2])
        except:
            cmds.spaceLocator(n = locName)
            cmds.setAttr(locName + ".tx", locInfo[i*8])
            cmds.setAttr(locName + ".ty", locInfo[i*8+1])
            cmds.setAttr(locName + ".tz", locInfo[i*8+2])
            
        cmds.setAttr(locName + ".rx", locInfo[i*8+3])
        cmds.setAttr(locName + ".ry", locInfo[i*8+4])
        cmds.setAttr(locName + ".rz", locInfo[i*8+5])

        if locInfo[i*8+6] > 0.5:
            cmds.setAttr(locName + ".sx", scaleX)
            cmds.setAttr(locName + ".sy", scaleX)
            cmds.setAttr(locName + ".sz", scaleX)
            
            cmds.setAttr(locName + ".v", 1)
        else:
            cmds.setAttr(locName + ".sx", bkScaleDef)
            cmds.setAttr(locName + ".sy", bkScaleDef)
            cmds.setAttr(locName + ".sz", bkScaleDef)
            
            cmds.setAttr(locName + ".v", 0)
            
    cmds.select("McdJALoc_*")
    cmds.setKeyframe()






    
    
    
    
