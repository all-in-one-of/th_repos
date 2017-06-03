
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
## TRADE PRACTICE. IN NO EVENT WILL BASEFOUNT AND/OR ITS LICENSORS 
## BE LIABLE FOR ANY LOST REVENUES, DATA, OR PROFITS, OR SPECIAL, 
## DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES, EVEN IF BASEFOUNTAIN 
## AND/OR ITS LICENSORS HAS BEEN ADVISED OF THE POSSIBILITY 
## OR PROBABILITY OF SUCH DAMAGES.
##
## ===================================================================
## -

## +
## ===================================================================
##  Module Name: McdRenderVRFunctions.py
##
##  Description:
##    eal with V-Ray Renderer stuffs
##
## ===================================================================
## -

import os
import shutil
import maya.cmds as cmds
import maya.mel as mel
from McdGeneral import *
try:
    from vray.utils import *
except:
    pass
import McdRenderFBXFunctions as RenderFBX

if int(mel.eval("getApplicationVersionAsFloat")) >= 2013:
    try:
        import mentalray.renderProxyUtils
    except:
        pass
else:
    try:
        import maya.app.mentalray.renderProxyUtils
    except:
        pass
    
def McdShowPPTC():
    cmds.confirmDialog(t = "Scripts", m = "Setup Render Setting > VRay Common > MEL/Python Callbacks\n\n" + \
                                    "from vray.utils import *\n" + \
                                    "McdVRayRender()")
    
def McdVRSetupPreSetup():
    
    McdLicenseCheck()
    checkSkinForAll()
    checkUVForAll()
    
    allAgents = cmds.ls(type = "McdAgent")
    if allAgents == [] or allAgents == None:
        cmds.confirmDialog(t = "Error", m = 'Please Place your agents firstly.')
        return
    
    globalNode = McdGetMcdGlobalNode()
    

    # read export path name from MGlobal
    outputPath = cmds.getAttr(globalNode + ".outputVRFolder")
    # read export file name from MGlobal
    outputName = cmds.getAttr(globalNode + ".outputVRName")
    
    # check availablity
    if outputPath == None:
        cmds.confirmDialog(t = "Error", m = "Cannot write vray file to disk, specify right path in: \nMiarmy > Render Global > Other Renders Tab")
        return;
    
    if not os.access(outputPath, os.W_OK):
        cmds.confirmDialog(t = "Error", m = "Cannot write vray file to disk, specify right path in: \nMiarmy > Render Global > Other Renders Tab")
        return;
    
    # create extra path
    try:
        os.makedirs(outputPath + "/" + outputName)
    except:
        pass
    
    if not os.access(outputPath + "/" + outputName, os.W_OK):
        cmds.confirmDialog(t = "Error", m = "Cannot write mi file to disk, specify right path in: \nMiarmy > Render Global > Other Renders Tab")
        return;

    try:
        if not os.access(outputPath + "/" + outputName + "/ProcPrimAssets", os.R_OK):
            os.makedirs(outputPath + "/" + outputName + "/ProcPrimAssets")
    except:
        pass
    
    try:
        if not os.access(outputPath + "/" + outputName + "/ProcPrimAssets/ClothData", os.R_OK):
            os.makedirs(outputPath + "/" + outputName + "/ProcPrimAssets/ClothData")
    except:
        pass
    
    try:
        if not os.access(outputPath + "/" + outputName + "/ProcPrimAssets/PoseData", os.R_OK):
            os.makedirs(outputPath + "/" + outputName + "/ProcPrimAssets/PoseData")
    except:
        pass
    
    if not os.access(outputPath + "/" + outputName + "/ProcPrimAssets", os.W_OK):
        cmds.confirmDialog(t = "Error", m = "Cannot write proc assets file to disk, specify right path in: \nMiarmy > Render Global > Other Renders Tab")
        return;
    
    exportFolder = outputPath + "/" + outputName + "/ProcPrimAssets"
    
    if not os.access(exportFolder, os.W_OK):
        try:
            os.mkdir(exportFolder)
        except:
            cmds.confirmDialog(t = "IO Error", m = exportFolder + " not writable, please specify right path in Miarmy Render Global ")
            return
    
    # get how many folders needed
    allAgentGrpNodes = cmds.ls(type = "McdAgentGroup")
    
    # create sub folders
    if allAgentGrpNodes == [] or allAgentGrpNodes == None:
        cmds.confirmDialog(t = "Abort", m = "Nothing to export.")
        return
        
    for i in range(len(allAgentGrpNodes)):
        if not os.access(exportFolder + "/McdAgentType" + str(i), os.W_OK):
            os.mkdir(exportFolder + "/McdAgentType" + str(i))
        if not os.access(exportFolder + "/McdAgentType" + str(i) + "/McdGeoFiles", os.W_OK):    
            os.mkdir(exportFolder + "/McdAgentType" + str(i) + "/McdGeoFiles")
    
    return globalNode
    
    
def McdVRSetupCurrentFrame_ExportingGeoTexRandInfo():
    
    checkUVForAll()
    McdSetupExportFlagForSpeicalMeshes()

    RenderFBX.clearUselessObjAndShadersVRay()
    
    McdLicenseCheck()
    checkSkinForAll()
    checkUVForAll()
    
    allAgents = cmds.ls(type = "McdAgent")
    if allAgents == [] or allAgents == None:
        cmds.confirmDialog(t = "Error", m = 'Please Place your agents firstly.')
        return
    
    
    globalNode = McdGetMcdGlobalNode()
    
    # read export path name from MGlobal
    outputPath = cmds.getAttr(globalNode + ".outputRCFolder")
    # read export file name from MGlobal
    outputName = cmds.getAttr(globalNode + ".outputRCName")
    
    try:
        if not os.access(outputPath, os.W_OK):
            cmds.confirmDialog(t = "Error", m = 'render catalog file path not writable.')
            return
    except:
        cmds.confirmDialog(t = "Error", m = 'Please specify the render catalog file path.')
        return

    
    # randomize textures:
    shaderPath = ""
    RenderFBX.McdRandomizeTexturesDSO("vray", shaderPath)

    McdVRSetupCurrentFrame_ByARMode(globalNode, 2)
    
def McdVRSetupCurrentFrame_ByARMode(globalNode, replaceMode = 0):
    
    allAgents = cmds.ls(type = "McdAgent")
    if allAgents == [] or allAgents == None:
        cmds.confirmDialog(t = "Error", m = 'Please Place your agents firstly.')
        return
    
    hideList = []
    allAgentGrps = cmds.ls(type = "McdAgentGroup")
    for i in range(len(allAgentGrps)):
        print allAgentGrps[i]
        if cmds.getAttr(allAgentGrps[i] + ".v") == 0:
            try:
                cmds.setAttr(allAgentGrps[i] + ".v", 1)
                hideList.append(allAgentGrps[i])
            except:
                pass
    
    allAgentGrps = cmds.ls("*Geometry_*")
    for i in range(len(allAgentGrps)):
        if cmds.getAttr(allAgentGrps[i] + ".v") == 0:
            try:
                cmds.setAttr(allAgentGrps[i] + ".v", 1)
                hideList.append(allAgentGrps[i])
            except:
                pass
    
    allAgentGrps = cmds.ls("*Miarmy_Contents*")
    for i in range(len(allAgentGrps)):
        if cmds.getAttr(allAgentGrps[i] + ".v") == 0:
            try:
                cmds.setAttr(allAgentGrps[i] + ".v", 1)
                hideList.append(allAgentGrps[i])
            except:
                pass
    
    if hideList!= []:
        for i in range(len(hideList)):
            try:
                cmds.setAttr(hideList[i] + ".v", 0)
            except:
                pass
    
    # after exporting, we need export ass geo file!!
    if replaceMode == 0:
        melCmd = "McdARPPExportCmd -em 51;" # exporting and combining!
    elif replaceMode == 1:
        melCmd = "McdARPPExportCmd -em 52;" # exporting without geo data
    elif replaceMode == 2:
        melCmd = "McdARPPExportCmd -em 58;" # exporting geo rand info
    mel.eval(melCmd)
    
def McdVRSetupCurrentFrame():
    
    checkUVForAll()
    McdSetupExportFlagForSpeicalMeshes()

    RenderFBX.clearUselessObjAndShadersVRay()
    globalNode = McdVRSetupPreSetup()
    
    # read export path name from MGlobal
    outputPath = cmds.getAttr(globalNode + ".outputVRFolder")
    # read export file name from MGlobal
    outputName = cmds.getAttr(globalNode + ".outputVRName")
    
    createVRInfoNode(outputPath, outputName)

    
    # randomize textures:
    shaderPath = ""
    RenderFBX.McdRandomizeTexturesDSO("vray", shaderPath)

    # export assets:
    melCmd = "McdARPPExportCmd -em 50;"
    mel.eval(melCmd)

    McdVRSetupCurrentFrame_ByARMode(globalNode)
    

def McdVRSetupAllFrame():
    
    checkUVForAll()
    McdSetupExportFlagForSpeicalMeshes()
    
    RenderFBX.clearUselessObjAndShadersVRay()
    globalNode = McdVRSetupPreSetup()
    
    # read export path name from MGlobal
    outputPath = cmds.getAttr(globalNode + ".outputVRFolder")
    # read export file name from MGlobal
    outputName = cmds.getAttr(globalNode + ".outputVRName")
    
    createVRInfoNode(outputPath, outputName)
    
    
    minFrame = cmds.playbackOptions(q = True, min = True)
    maxFrame = cmds.playbackOptions(q = True, max = True)
    nbFrame = int(maxFrame - minFrame + 1)
    
    stat = cmds.confirmDialog(t = "Note", m = "Export vray ready file from " + str(minFrame) + " to " + str(maxFrame) + "\n" + \
                                     "We recommend you save your sence before exporting, continue?", b = ["Proceed", "Cancel"])
    
    if stat == "Cancel":
        return;
    
    # create box and naming it to McdMRRenderDummy
    dummyGrpTemp = cmds.ls("McdVRRenderDummy_Grp")
    dummyGrp = ""
    if dummyGrpTemp != [] and dummyGrpTemp != None:
        dummyGrp = dummyGrpTemp[0]
    if dummyGrp == "":
        cmds.select(clear = True)
        cmds.group(n = "McdVRRenderDummy_Grp", em = True)
    
    # ############################################################
    # randomize textures:
    shaderPath = outputPath + '/' + outputName + '/mat' + outputName + '.mi'
    duplicatedObject = RenderFBX.McdRandomizeTexturesDSO("vray", shaderPath)
    
    cmd = "McdAgentMatchCmd -mm 0;"
    mel.eval(cmd)
    
    # export assets
    melCmd = "McdARPPExportCmd -em 50;"
    mel.eval(melCmd)
    
    
    # real export 
    totalCount = nbFrame
    
    for i in range(nbFrame):
        
        frameNumberNum = minFrame + i
        cmds.currentTime(frameNumberNum)
        
        try:
            McdVRSetupCurrentFrame_ByARMode(globalNode)
            cmd = "McdAgentMatchCmd -mm 0;"
            mel.eval(cmd)
        except:
            raise Exception("Cannot export ")


def McdVRSetupAllFrameReplaceMat():
    
    RenderFBX.clearUselessObjAndShadersVRay()
    globalNode = McdVRSetupPreSetup()
    
    # read export path name from MGlobal
    outputPath = cmds.getAttr(globalNode + ".outputVRFolder")
    # read export file name from MGlobal
    outputName = cmds.getAttr(globalNode + ".outputVRName")
    
    createVRInfoNode(outputPath, outputName)

    
    # randomize textures:
    shaderPath = ""
    RenderFBX.McdRandomizeTexturesDSO("vray", shaderPath)

    # export assets:
    melCmd = "McdARPPExportCmd -em 50;"
    mel.eval(melCmd)

    McdVRSetupCurrentFrame_ByARMode(globalNode, 1)
    
    McdVRCopyAndReplaceMat(globalNode)


def McdVRCopyAndReplaceMat(globalNode):
    # copy pose data folder all contents
    # read and record mat
    # for each file
    #   read original lines
    #   encounter mat
    #   write new one
    
    outputPath = cmds.getAttr(globalNode + ".outputVRFolder")
    outputName = cmds.getAttr(globalNode + ".outputVRName")
    
    outputOldName = cmds.getAttr(globalNode + ".outputVRNewName")
    
    # copy pose data folder all contents
    poseDataFolder_org = outputPath + "/" + outputOldName + "/ProcPrimAssets/PoseData"
    poseDataFolder_new = outputPath + "/" + outputName + "/ProcPrimAssets/PoseData"
    
    allPoseFiles = os.listdir(poseDataFolder_org)
    if allPoseFiles == None or allPoseFiles == []:
        raise Exception("Didn't find the pose files")
        return;
    
    for i in range(len(allPoseFiles)):
        shutil.copy(poseDataFolder_org + "/" + allPoseFiles[i], poseDataFolder_new + "/" + allPoseFiles[i])
        
    
    # read and record mat
    matFile = outputPath + "/" + outputName + "/_mat_" + outputName + ".txt"
    allMats = []
    f = open(matFile, "r")
    matContentsRawStr = f.read()
    f.close()
    
    if matContentsRawStr.find("\r\n") >= 0:
        splitter = "\r\n"
    else:
        splitter = "\n"
        
    matList = matContentsRawStr.split(splitter)
    nbMat = len(matList)
    
    newGeoFolder = outputPath + "/" + outputName
    oldGeoFolder = outputPath + "/" + outputOldName
    allOrgFilesRaw = os.listdir(oldGeoFolder)
    findName = "geo" + outputOldName
    newFileName = "geo" + outputName
    findTxt = ".txt"
    if allOrgFilesRaw == [] or allOrgFilesRaw == None:
        raise Exception("Didn't find old geo files")
        return
    
    
    totalCount = len(allOrgFilesRaw)
    
    
    # for each file
    for i in range(len(allOrgFilesRaw)): 
        if allOrgFilesRaw[i].find(findName) == 0 and allOrgFilesRaw[i].find(findTxt) > 0:
            orgGeoFile = oldGeoFolder + "/" + allOrgFilesRaw[i]
            
            # get frame number:
            frameStrRaw = allOrgFilesRaw[i].split(findName)[1]
            frameStr = frameStrRaw.split(".txt")[0]
            
            newGeoFile = newGeoFolder + "/geo" + outputName + frameStr + ".txt"

            counter = 0
            f2Str = ""
            f1 = open(orgGeoFile, 'r')
            #   read original lines
            for currentLine in f1:
                #   encounter mat
                if currentLine.find('material "') == 0:
                    splitParts = currentLine.split('"')
                    f2Line = splitParts[0] + '"' + matList[counter] + '"' + splitParts[-1]
                    f2Str += f2Line
                    
                    counter += 1
                    if counter >= nbMat:
                        break
                    
                else:
                    f2Str += currentLine
                    
            f1.close()
            
            # write f2:
            f2 = open(newGeoFile, "w")
            f2.write(f2Str)
            f2.close()
            print newGeoFile
            
    
def McdGetVRExtraInfo(extraFile):
    
    resultData = []
    
    if not os.access(extraFile, os.R_OK):
        return resultData
    
    f = open(extraFile)
    contents = f.read()
    f.close()

    splitor = '\n'
    if contents.find('\r\n') >0:
        splitor = '\r\n'
    segs = contents.split(splitor)
    
    if segs != [] and segs != None and segs != "":
        for i in range(len(segs)):
            resultData.append(segs[i])
            
    return resultData
    
def McdGetVRGeomInfo(proxyFile):
    
    resultData = []
    
    f = open(proxyFile)
    contents = f.read()
    f.close()
    
    segs = contents.split('\n')
    nbObj = len(segs) / 15
    
    for i in range(nbObj):
        currentData = []
        # ppID (int)
        dataStr = segs[i*15 + 0]
        dataRaw = dataStr.split(" ")[-1]
        dataGet = int(dataRaw)
        currentData.append(dataGet)
        
        # agentID (int)
        dataStr = segs[i*15 + 1]
        dataRaw = dataStr.split(" ")[-1]
        dataGet = int(dataRaw)
        currentData.append(dataGet)
        
        # agentIndex (int)
        dataStr = segs[i*15 + 2]
        dataRaw = dataStr.split(" ")[-1]
        dataGet = int(dataRaw)
        currentData.append(dataGet)
        
        # geoID (int)
        dataStr = segs[i*15 + 3]
        dataRaw = dataStr.split(" ")[-1]
        dataGet = int(dataRaw)
        currentData.append(dataGet)
        
        # clothID (int)
        dataStr = segs[i*15 + 4]
        dataRaw = dataStr.split(" ")[-1]
        dataGet = int(dataRaw)
        currentData.append(dataGet)
        
        # currentFrame (int)
        dataStr = segs[i*15 + 5]
        dataRaw = dataStr.split(" ")[-1]
        dataGet = int(dataRaw)
        currentData.append(dataGet)
        
        # poly0_subd1 (int)
        dataStr = segs[i*15 + 6]
        dataRaw = dataStr.split(" ")[-1]
        dataGet = int(dataRaw)
        currentData.append(dataGet)
        
        # motionBlur (int)
        dataStr = segs[i*15 + 7]
        dataRaw = dataStr.split(" ")[-1]
        dataGet = int(dataRaw)
        currentData.append(dataGet)
        
        # motionShutter (float)
        dataStr = segs[i*15 + 8]
        dataRaw = dataStr.split(" ")[-1]
        dataGet = float(dataRaw)
        currentData.append(dataGet)
        
        # assetsPath (string)
        dataStr = segs[i*15 + 9]
        dataGet = dataStr.split('"')[1]
        currentData.append(dataGet)
        
        # bbox (string)
        dataStr = segs[i*15 + 10]
        dataGet = dataStr.split('"')[1]
        currentData.append(dataGet)
        
        # poseData (string)
        dataStr = segs[i*15 + 11]
        dataGet = dataStr.split('"')[1]
        currentData.append(dataGet)
        
        resultData.append(currentData)
        
    return resultData
    
def McdVRayRender(frameOffset = 0):
    # read python file
    # parse object
    # for each one:
        # parse each one param
    
    try:
        globalNode = cmds.ls("McdVRayInfoHost")[0]
    except:
        pass

    outputPath = cmds.getAttr(globalNode + ".outputVRFolder")
    outputName = cmds.getAttr(globalNode + ".outputVRName")
    

    # frame and pading:
    frameNumberNum = cmds.getAttr("time1.outTime")
    frameNumber = str(int(frameNumberNum) + frameOffset)
    while(len(frameNumber) < 4):
        frameNumber = "0" + frameNumber

    proxyFile = outputPath + "/" + outputName + "/" + "geo" + outputName + "."  + frameNumber + ".txt"
    extraFile = outputPath + "/" + outputName + "/" + "extra" + outputName + "."  + frameNumber + ".txt"
    
    geomInfo = McdGetVRGeomInfo(proxyFile)
    extraInfo = McdGetVRExtraInfo(extraFile)
    
    containExtra = False
    if extraInfo != []:
        containExtra = True
    
    for i in range(len(geomInfo)):
        objMat = geomInfo[i][11]
        
        newNode = create('Node', 'McdNode' + str(i) + '@node')
        newMesh = create('McdVRGeom', 'Mcd@mesh' + str(i) + '@mesh')
        newMesh.set("bbox_size", float(i) * 0.1)
        
        newMesh.set("ppID",         geomInfo[i][0])
        newMesh.set("agentID",      geomInfo[i][1])
        newMesh.set("agentIndex",   geomInfo[i][2])
        newMesh.set("geoID",        geomInfo[i][3])
        newMesh.set("clothID",      geomInfo[i][4])
        newMesh.set("currentFrame", geomInfo[i][5])
        newMesh.set("poly0_subd1",  geomInfo[i][6])
        newMesh.set("motionBlur",   geomInfo[i][7])
        newMesh.set("motionShutter",geomInfo[i][8])
        newMesh.set("assetsPath",   geomInfo[i][9])
        newMesh.set("bbox",         geomInfo[i][10])
        
        newNode.set('geometry', newMesh)
        newNode.set("visible",1)
        #newNode.set("primary_visibility",0)
        tr=Transform(1)
        shaderNode = exportMaterial(objMat)
        newNode.set('material', shaderNode)
        newNode.set("transform",tr)
        if containExtra:
            if extraInfo[i] == "-":
                newNode.set("user_attributes", "")
            else:
                fillStr = extraInfo[i]
                try:
                    fillStr = findAndReplaceExtraInfo(fillStr, i)
                except:
                    pass
                try:
                    fillStr = findAndReplaceExtraInfo2(fillStr, i)
                except:
                    pass
                try:
                    if fillStr.find("AGENTID") >= 0:
                        fillStr = findAndReplaceAgentIDInfo(fillStr, geomInfo[i][2])
                except:
                    pass
                try:
                    if fillStr.find("RAND_RGB_AGENT") >= 0:
                        fillStr = findAndReplaceAgentColor(fillStr, geomInfo[i][2])
                except:
                    pass
                try:
                    if fillStr.find("RAND_RGB_OBJECT") >= 0:
                        fillStr = findAndReplaceObjectColor(fillStr, i)
                except:
                    pass
                newNode.set("user_attributes", fillStr)
    
    
def createVRInfoNode(outF, outN):
    cmds.select(clear = True)
    vrnode = cmds.ls("*McdVRayInfoHost*")
    if not MIsBlank(vrnode):
        try:
            cmds.delete(vrnode)
        except:
            pass
    loc = cmds.spaceLocator(n = "McdVRayInfoHost")[0]
    
    cmds.addAttr(loc, ln = "outputVRFolder", dt = "string")
    cmds.addAttr(loc, ln = "outputVRName", dt = "string")
    
    cmds.setAttr(loc + ".outputVRFolder", outF, type = "string")
    cmds.setAttr(loc + ".outputVRName", outN, type = "string")
        
    
def findAndReplaceExtraInfo(extraStr, geoSeed):
    if extraStr.find("RAND[") >= 0:
        allSegs = extraStr.split("RAND[")
        if len(allSegs) > 1:
            resultStr = ""
            for i in range(len(allSegs)):
                if allSegs[i].find("]") > 0:
                    idx = allSegs[i].find("]")
                    numStr = allSegs[i][0:idx]
                    restStr = allSegs[i][idx+1:len(allSegs[i])]
                    
                    resultData = 0.0
                    numSegs = numStr.split(",")
                    if len(numSegs) > 1:
                        num1 = float(numSegs[0])
                        num2 = float(numSegs[1])
                        
                        resultNumRaw = McdSolveASeedMinMax(geoSeed, 17.79437 + float(i), num1, num2)
                        resultNumStr = str(resultNumRaw)
                        
                        if numSegs[0].find(".") < 0:
                            resultNumStr = str(int(resultNumRaw))
                    
                    resultStr += resultNumStr + restStr
                else:
                    resultStr += allSegs[i]
                    
            return resultStr
        
    return extraStr
    

def findAndReplaceExtraInfo2(extraStr, geoSeed):
    if extraStr.find("RAND<") >= 0:
        allSegs = extraStr.split("RAND<")
        if len(allSegs) > 1:
            resultStr = ""
            for i in range(len(allSegs)):
                if allSegs[i].find(">") > 0:
                    idx = allSegs[i].find(">")
                    numStr = allSegs[i][0:idx]
                    restStr = allSegs[i][idx+1:len(allSegs[i])]
                    
                    resultData = 0.0
                    numSegs = numStr.split(",")
                    if len(numSegs) > 1:
                        num1 = float(numSegs[0])
                        num2 = float(numSegs[1])
                        
                        resultNumRaw = McdSolveASeedMinMax(geoSeed, 17.79437, num1, num2)
                        resultNumStr = str(resultNumRaw)
                        
                        if numSegs[0].find(".") < 0:
                            resultNumStr = str(int(resultNumRaw))
                    
                    resultStr += resultNumStr + restStr
                else:
                    resultStr += allSegs[i]
                    
            return resultStr
        
    return extraStr
    
    
def findAndReplaceAgentIDInfo(fillStr, agentID):
    aidStr = str(agentID+1)
    fillStr = fillStr.replace("AGENTID", aidStr)
    
    return fillStr
    
    
def findAndReplaceAgentColor(fillStr, agentID):
    
    color0 = McdSolveASeedMinMax(agentID, 17.79437, 0.0, 1.0)
    color1 = McdSolveASeedMinMax(agentID, 18.79437, 0.0, 1.0)
    color2 = McdSolveASeedMinMax(agentID, 19.79437, 0.0, 1.0)
    
    resultStr = str(color0) + "," + str(color1) + "," + str(color2)
    
    fillStr = fillStr.replace("RAND_RGB_AGENT", resultStr)
    
    return fillStr
    
    
    
def findAndReplaceObjectColor(fillStr, i):
    
    color0 = McdSolveASeedMinMax(i, 17.79437, 0.0, 1.0)
    color1 = McdSolveASeedMinMax(i, 18.79437, 0.0, 1.0)
    color2 = McdSolveASeedMinMax(i, 19.79437, 0.0, 1.0)
    
    resultStr = str(color0) + "," + str(color1) + "," + str(color2)
    
    fillStr = fillStr.replace("RAND_RGB_AGENT", resultStr)
    
    return fillStr




    
    
    
