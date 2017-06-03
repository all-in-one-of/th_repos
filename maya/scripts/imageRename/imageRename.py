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
    print "\n--------------------����Ϊ��ͼ�����б�---------------------"
    print "------------------���ļ��� to : ���ļ���---------------------"
    if pm.checkBox('renameDoItCBX',q=1,v=1): 
        print 	"----------------------ִ��---------------------"
    elif pm.checkBox('renameDoItCBX',q=1,v=1)==0:
        print "----------------------Ԥ��---------------------"
    if len(_s)>0:
        for s in _s:
            inputName = _inputName
            a = '#'
            b = '$' 
            if pm.nodeType(s) == 'file':
                oldImageLName = s.fileTextureName.get()
                if len(oldImageLName)>0:
                    try:    
                #������ĸ����ʽ                
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
                                print "%s:����ļ��Ѵ���,����!" % str(newImageLNmae)
                            elif 'ext:' in inputName and ',' in inputName:
                                if inputName.split(':')[-1].split(',')[-2] == fileExt:
                                    if os.path.exists(newImageLNmae.replace(fileExt,nfileExt)):
                                        print (oldImageSName + fileExt + ' to: ' + newImageSName + nfileExt)   
                                    else:
                                        print "���������޸��ļ���ʽ�����%s�ļ�������" % str(newImageLNmae.replace(fileExt,nfileExt))
                                else:
                                    print "�������󣺵�ǰ�ļ���ʽΪ��%s,��ȴ��Ҫ��%s��ʽ�ĳ�%s,��������" % (str(fileExt),str(inputName.split(':')[-1].split(',')[-2]),str(nfileExt))
                            else:
                                print  (oldImageSName + fileExt + ' to: ' + newImageSName + nfileExt)						
                        if pm.checkBox('renameDoItCBX',q=1,v=1):
                            try:
                                if 'ext:' in inputName and ',' in inputName:
                                    if inputName.split(':')[-1].split(',')[-2] == fileExt:
                                        if os.path.exists(newImageLNmae.replace(fileExt,nfileExt)):                                            
                                            s.fileTextureName.set(newImageLNmae.replace(fileExt,inputName.nfileExt))
                                        else:
                                            print "���������޸��ļ���ʽ�����%s�ļ�������" % str(newImageLNmae.replace(fileExt,nfileExt))
                                    else:
                                        print "�������󣺵�ǰ�ļ���ʽΪ��%s,��ȴ��Ҫ��%s��ʽ�ĳ�%s,��������" % (str(fileExt),str(inputName.split(':')[-1].split(',')[-2]),str(nfileExt))
                                else:
                                    if pm.checkBox('reFileToDo',q=1,v=1):
                                        os.rename(oldImageLName,newImageLNmae)
                                    s.fileTextureName.set(newImageLNmae)
                                    print  (oldImageSName + fileExt + ' to: ' + newImageSName + nfileExt)
                                    print "�Ѹ�����"
                            except:
                                print "��������%s:����ļ��е����⣬����û��Ȩ�޻���������ʽ���Ե����ļ����ܸ���������!" % str(oldImageLName)
                        n+=1
                        i+=1
                        if i > 122:
                            i=65
                        if 90<i <97:
                            #print "��ѡ�е�file�ڵ�̫�࣬��$���ܳ���52��,�����Ĳ������������ֱ�ʾ����0��ʼ����!"
                            i=48
                        index += 1
                    except:
                        print "%s������ڵ���ļ��г�ͻ��" % str(s)
                else:                    
                    print "%s������ڵ���ļ������ڣ�" % str(s)
            else:
                print "%s����ǰѡ�еĲ���File�ڵ㣡" % str(s)
                
    else:
        print "��ѡ��һ������FileNode��"
        
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
        print "ѡ�еĲ���file�ڵ�ɣ�"
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
    pm.menuItem(l='���ø�ʽ��             *',c= 'pm.textField("FIRtexField",e=1,tx="*")' )
    pm.menuItem(l='    ��dfǰ׺��           df*',c= 'pm.textField("FIRtexField",e=1,tx="df*")' )
    pm.menuItem(l='    ����ɫ��׺��       *_Diff',c= 'pm.textField("FIRtexField",e=1,tx="*_Diff")' )
    pm.menuItem(l='    �ӷ��ߺ�׺��       *_Norm',c= 'pm.textField("FIRtexField",e=1,tx="*_Norm")' )
    pm.menuItem(l='    �Ӹ߹��׺��       *_Spec',c= 'pm.textField("FIRtexField",e=1,tx="*_Spec")' )
    pm.menuItem(l='    �Ӱ�͹��׺��       *_Bump',c= 'pm.textField("FIRtexField",e=1,tx="*_Bump")' )
    pm.menuItem(l='    �����ֺ�׺��       *_Mask',c= 'pm.textField("FIRtexField",e=1,tx="*_Mask")' )
    pm.menuItem(l='    ���û���׺��       *_Disp',c= 'pm.textField("FIRtexField",e=1,tx="*_Disp")' )
    pm.menuItem(l='    �����ֱ�ţ�       *#',c= 'pm.textField("FIRtexField",e=1,tx="*#")' )
    pm.menuItem(l='    ����ĸ��ţ�       *$',c= 'pm.textField("FIRtexField",e=1,tx="*$")' )
    pm.menuItem(l='    �滻���֣�         abcd,ABCD',c= 'pm.textField("FIRtexField",e=1,tx="abcd,ABCD")' )
    pm.menuItem(l='    �滻��ʽ(���޸�file�ڵ�)��         ext:*,*',c= 'pm.textField("FIRtexField",e=1,tx="ext:.jpg,.tif")' )
    #pm.menuItem(l='��ȡѡ�е�һ��������',c= ' pm.textField( "FIRtexField",e=1,tx= os.path.splitext( pm.ls(sl=1)[0].fileTextureName.get().split("/")[-1])[0]" ) ' )
    pm.checkBox('renameDoItCBX',l="doIt",v=0,ann = "��ѡ��ִ��������ȥ�����鿴����Ԥ�����")
    pm.checkBox('reFileToDo',l="reFile",v=1,ann="��ѡ��,ͬʱ�޸���ͼ�ļ�����ȥ�����޸�file�ڵ��е�imageName")
    pm.button(l="rename",c='renameImage()',bgc = (random.uniform(0.1,1),random.uniform(0.1,1),random.uniform(0.1,1)),ann = "����������\"*\"                 ����ԭʼ����;\n	     \"#\"                ����������������;\n	     \"$\"                ������ĸa-z,A-Z��������;\n	     \"abcd,ABCD\"����abcd�滻��ABCD,��\",\"����;\n	     \"abcd, \"         ����ȥ��\",\"ǰ������")
    pm.popupMenu(markingMenu =1)
    pm.menuItem(l='��õ�ǰ��ͼ����',radialPosition = 'E',c='getCurrentFileName()')
    pm.menuItem(l='ѡ�е�ǰ��ͬ��ͼ��file�ڵ�',radialPosition = 'W',c='getCurrentEqualFileName()')
    pm.menuItem(l='ѡ��Arnold diffuse��',c='pm.select(selectType("aiStandard:diffuse"))')
    pm.menuItem(l='ѡ��Arnold specular��',c='pm.select(selectType("aiStandard:specular"))')
    pm.menuItem(l='ѡ��Arnold reflection��',c='pm.select(selectType("aiStandard:reflection"))')
    pm.menuItem(l='ѡ��Arnold refraction',c='pm.select(selectType("aiStandard:refraction"))')
    pm.menuItem(l='ѡ��bump��',c='pm.select(selectType("bump2d:bump"))')
    pm.showWindow('renameFileImages')
    
