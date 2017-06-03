# -*- coding: utf-8 -*-
#author:jarry,61692940@qq.com


import pymel.core as pm
import random
import os
def renameImage():
    _s = pm.ls(sl=1,type='file')
    _inputName = pm.textField("FIRtexField",q=1,tx=1)
    n=1
    i = 97
    index = 0
    print "\n--------------------以下为贴图改名列表---------------------"
    print "------------------旧文件名 to : 新文件名---------------------"
    if pm.checkBox('renameDoItCBX',q=1,v=1): 
        print 	"----------------------执行---------------------"
    elif pm.checkBox('renameDoItCBX',q=1,v=1)==0:
        print "----------------------预览---------------------"
    if len(_s)>0:
        for s in _s:
            inputName = _inputName
            a = '#'
            b = '$' 
            if pm.nodeType(s) == 'file':
                oldImageLName = s.fileTextureName.get()
                if len(oldImageLName)>0:
                    try:    
                #超量字母排序方式                
                        if '$' in inputName:
                            if index>25:
                                abcNumber = chr(index/26+64)+chr(index%26 + 65)
                            else:
                                abcNumber = chr(index%26 + 65)
                            inputName = inputName.replace('$',abcNumber)
                                            
                        oldImageSName = os.path.splitext(oldImageLName.split('/')[-1])[0]
                        fileExt = os.path.splitext(oldImageLName.split('/')[-1])[-1]
                        nfileExt = fileExt
                        newImageSName = inputName 
                        if '*' in inputName or a in inputName or b in inputName:
                            newImageSName = inputName.replace('*',oldImageSName).replace(a,str(n)).replace('$',chr(i))
                            #inputName = newImageSName
                        if ',' in inputName:
                            newImageSName = oldImageSName.replace(inputName.split(',')[0],inputName.split(',')[-1])
                            if 'ext:' in inputName and ',' in inputName:
                                nfileExt = inputName.split(',')[-1]
                            if '*' in inputName or a in inputName or b in inputName:
                                newImageSName = newImageSName.replace('*',oldImageSName).replace(a,str(n)).replace('$',chr(i))
                        newImageLNmae = oldImageLName.replace(oldImageSName,newImageSName)#.replace(fileExt,nfileExt)
                        if pm.checkBox('renameDoItCBX',q=1,v=1)==0:
                            if os.path.exists(newImageLNmae)==1 and newImageLNmae != oldImageLName:
                                print "%s:这个文件已存在,请检查!" % str(newImageLNmae)
                            elif 'ext:' in inputName and ',' in inputName:
                                if inputName.split(':')[-1].split(',')[-2] == fileExt:
                                    if os.path.exists(newImageLNmae.replace(fileExt,nfileExt)):
                                        print (oldImageSName + fileExt + ' to: ' + newImageSName + nfileExt)   
                                    else:
                                        print "命名错误：修改文件格式：你的%s文件不存在" % str(newImageLNmae.replace(fileExt,nfileExt))
                                else:
                                    print "命名错误：当前文件格式为：%s,你却想要把%s格式改成%s,请修正！" % (str(fileExt),str(inputName.split(':')[-1].split(',')[-2]),str(nfileExt))
                            else:
                                print  (oldImageSName + fileExt + ' to: ' + newImageSName + nfileExt)						
                        if pm.checkBox('renameDoItCBX',q=1,v=1):
                            try:
                                if 'ext:' in inputName and ',' in inputName:
                                    if inputName.split(':')[-1].split(',')[-2] == fileExt:
                                        if os.path.exists(newImageLNmae.replace(fileExt,nfileExt)):                                            
                                            s.fileTextureName.set(newImageLNmae.replace(fileExt,inputName.nfileExt))
                                        else:
                                            print "命名错误：修改文件格式：你的%s文件不存在" % str(newImageLNmae.replace(fileExt,nfileExt))
                                    else:
                                        print "命名错误：当前文件格式为：%s,你却想要把%s格式改成%s,请修正！" % (str(fileExt),str(inputName.split(':')[-1].split(',')[-2]),str(nfileExt))
                                else:
                                    if pm.checkBox('reFileToDo',q=1,v=1):
                                        os.rename(oldImageLName,newImageLNmae)
                                    s.fileTextureName.set(newImageLNmae)
                                    print  (oldImageSName + fileExt + ' to: ' + newImageSName + nfileExt)
                                    print "已改名！"
                            except:
                                print "命名错误：%s:这个文件有点问题，可能没有权限或者命名格式不对导致文件不能改名，请检查!" % str(oldImageLName)
                        n+=1
                        i+=1
                        if i > 122:
                            i=65
                        if 90<i <97:
                            #print "你选中的file节点太多，用$不能超过52个,超过的部分现在用数字表示，从0开始算起!"
                            i=48
                        index += 1
                    except:
                        print "%s：这个节点的文件有冲突！" % str(s)
                else:                    
                    print "%s：这个节点的文件不存在！" % str(s)
            else:
                print "%s：当前选中的不是File节点！" % str(s)
                
    else:
        print "请选中一个或多个FileNode！"
        
def selectType(_inputName):
    attrDist = {'diffuse':['color','Kd','diffuseRoughness','Kb','KsssColor','Ksss','sssRadius'],'specular':['KsColor','Ks','specularRoughness','specularAnisotropy','specularRotation'],'reflection':['KrColor','Kr'],'refraction':['KtColor','Kt','IOR','dispersionAbbe','refractionRoughness'],'bump':['bumpValue','bumpMap']}
    #inputName = pm.textField("FIRtexField",q=1,tx=1)
    inputName = _inputName
    attrFile = []
    if ':' in inputName:
        nodeType = inputName.split(':')[0]
        attrType = inputName.split(':')[1]
        for s in pm.ls(type = nodeType):
            #print s
            for ss in attrDist.get(attrType):
                #print ss
                if s.hasAttr(ss):
                    for sss in pm.listConnections(s +"." + ss):
                        print sss
                        attrFile.append(sss)
    attrFile = list(set(attrFile))    		
    return attrFile
def getCurrentFileName():
    if pm.ls(sl=1)[0].type() == "file":
        pm.textField( "FIRtexField",e=1,tx= os.path.splitext( pm.ls(sl=1)[0].fileTextureName.get().split("/")[-1])[0] )
def getCurrentEqualFileName():
    xiangtongNode = []
    listFileNode = pm.ls(type='file')
    try:        
        listFileNode.remove(pm.ls(sl=1)[0])
        #print listFileNode
    except:
        print "选中的不是file节点吧！"
    for s in pm.ls(type='file'):
        currenSLName = os.path.splitext( pm.ls(sl=1)[0].fileTextureName.get().split("/")[-1])[0]
        sName =  os.path.splitext( s.fileTextureName.get().split("/")[-1])[0]
        if currenSLName == sName:
            #print "have!"
            xiangtongNode.append(s)
    print xiangtongNode
    xiangtongNode.remove(pm.ls(sl=1)[0])
    print xiangtongNode
    if len(xiangtongNode)>0:
        pm.select(xiangtongNode)
    print len(xiangtongNode)                
        

def UI():
    if pm.window('renameFileImages', exists=True):
        pm.deleteUI('renameFileImages', window=True)
    pm.window( 'renameFileImages',widthHeight=(352, 32),s=0)
    buttonColor1 = (0.6,0.6,0.55)
    buttonColor2 = (0.65,0.65,0.55)
    pm.rowColumnLayout( numberOfColumns=4,h = 30,columnWidth=[(1, 180), (2, 50), (3, 60),(4, 60)])
    pm.textField('FIRtexField',tx='*',h=30)
    pm.popupMenu()
    pm.menuItem(l='常用格式：             *',c= 'pm.textField("FIRtexField",e=1,tx="*")' )
    pm.menuItem(l='    加df前缀：           df*',c= 'pm.textField("FIRtexField",e=1,tx="df*")' )
    pm.menuItem(l='    加颜色后缀：       *_Diff',c= 'pm.textField("FIRtexField",e=1,tx="*_Diff")' )
    pm.menuItem(l='    加法线后缀：       *_Norm',c= 'pm.textField("FIRtexField",e=1,tx="*_Norm")' )
    pm.menuItem(l='    加高光后缀：       *_Spec',c= 'pm.textField("FIRtexField",e=1,tx="*_Spec")' )
    pm.menuItem(l='    加凹凸后缀：       *_Bump',c= 'pm.textField("FIRtexField",e=1,tx="*_Bump")' )
    pm.menuItem(l='    加遮罩后缀：       *_Mask',c= 'pm.textField("FIRtexField",e=1,tx="*_Mask")' )
    pm.menuItem(l='    加置换后缀：       *_Disp',c= 'pm.textField("FIRtexField",e=1,tx="*_Disp")' )
    pm.menuItem(l='    加数字编号：       *#',c= 'pm.textField("FIRtexField",e=1,tx="*#")' )
    pm.menuItem(l='    加字母编号：       *$',c= 'pm.textField("FIRtexField",e=1,tx="*$")' )
    pm.menuItem(l='    替换名字：         abcd,ABCD',c= 'pm.textField("FIRtexField",e=1,tx="abcd,ABCD")' )
    pm.menuItem(l='    替换格式(仅修改file节点)：         ext:*,*',c= 'pm.textField("FIRtexField",e=1,tx="ext:.jpg,.tif")' )
    #pm.menuItem(l='获取选中第一个的名字',c= ' pm.textField( "FIRtexField",e=1,tx= os.path.splitext( pm.ls(sl=1)[0].fileTextureName.get().split("/")[-1])[0]" ) ' )
    pm.checkBox('renameDoItCBX',l="doIt",v=0,ann = "勾选后执行命名，去勾，查看命名预览结果")
    pm.checkBox('reFileToDo',l="reFile",v=1,ann="勾选后,同时修改贴图文件名，去勾仅修改file节点中的imageName")
    pm.button(l="rename",c='renameImage()',bgc = (random.uniform(0.1,1),random.uniform(0.1,1),random.uniform(0.1,1)),ann = "批量改名：\"*\"                 代表原始名字;\n	     \"#\"                代表数字依次排序;\n	     \"$\"                代表字母a-z,A-Z依次排序;\n	     \"abcd,ABCD\"代表abcd替换成ABCD,用\",\"区分;\n	     \"abcd, \"         代表去掉\",\"前的名字")
    pm.popupMenu(markingMenu =1)
    pm.menuItem(l='获得当前贴图名字',radialPosition = 'E',c='getCurrentFileName()')
    pm.menuItem(l='选中当前相同贴图的file节点',radialPosition = 'W',c='getCurrentEqualFileName()')
    pm.menuItem(l='选中Arnold diffuse类',c='pm.select(selectType("aiStandard:diffuse"))')
    pm.menuItem(l='选中Arnold specular类',c='pm.select(selectType("aiStandard:specular"))')
    pm.menuItem(l='选中Arnold reflection类',c='pm.select(selectType("aiStandard:reflection"))')
    pm.menuItem(l='选中Arnold refraction',c='pm.select(selectType("aiStandard:refraction"))')
    pm.menuItem(l='选中bump类',c='pm.select(selectType("bump2d:bump"))')
    pm.showWindow('renameFileImages')
    
