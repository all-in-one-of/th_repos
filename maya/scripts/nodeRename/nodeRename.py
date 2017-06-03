# -*- coding: utf-8 -*-
#author:jarry,61692940@qq.com
import pymel.core as pm
import random
import os
import maya.mel as mel
import maya.cmds as cmds
import random
import re
import json

class nodeRename(object):
    def __init__(self):
        self._s = pm.ls(sl=1)
        self._rule = ['*',',','-','|','#','$',':','.']
        self._typeDict = {'aiStandard':'mat','aiSkin':'mat','blinn':'mat','lambert':'mat','phong':'mat','layeredShader':'mat','mesh':'msh','group':'grp','Mesh':'msh','Light':'lit'}
        self._currenpath = os.path.dirname(__file__).replace('\\','/')
        self._nodeTypePath = self._currenpath + r'/jason/nodeType.json'
    
    def get_json_data(self,path):
        """
        ��������json���ݵ������
        Args:
            path: �ַ���,json�����ļ���������·��

        Returns:
            ����json�ļ��ڵ�����
        """
        if os.path.isfile(path):
            f = open(path, 'r')
            data = json.loads(f.read())
            f.close()
            return data
        else:
            return False
            
    def addSG(self):
        selectList = pm.ls(sl=1)
        if len(selectList)>0:
            for s in self.selectList:
                pm.rename(s.shadingGroups()[0],s+"SG")
        else:
            print "��ѡ��һ������shader��"
            
    def addMat(self):
        selectList = pm.ls(sl=1)
        if len(selectList)>0:
            for s in self.selectList:
                if '_mat' not in str(s):
                    pm.rename(s,s+"_mat")
        else:
            print "��ѡ��һ������shader��"
			
    def isInt(self,S):
        try:
            x=int(S)
            return isinstance(x,int)
        except ValueError:
            return False   
			
    def renmaeNode(self,_inputName):
        inputName = _inputName
        
        typeDict = self.get_json_data(self._nodeTypePath)
        if typeDict == False:
            print "û��json�ļ�"
            typeDict = self._typeDict
            
        n = 1
        i = 97
        selectList = pm.ls(sl=1)
        if len(selectList)>0:
            for s in selectList:
                a = '#'
                b = '$'
                x = chr(i)
                children = []
                oldLongName = s.longName()
                oldShortName = s.longName().split('|')[-1]
                newName = inputName
        #������ʽ ̰����
                if '[' in inputName and ']' in inputName:
                    rule = inputName[inputName.find('[')+1:inputName.find(']')].replace('*','\w+')                        
                    if ':' not in rule:
                        try:
                            fixName = re.findall(rule,oldShortName)[0]
                        except:
                            print "������ʽ��ʽ�������,��鿴������"
                            break
                    elif ':' in rule:          
                        fixName = eval('oldShortName' + '['+rule+']')
                    inputName = inputName.replace(inputName[inputName.find('['):inputName.find(']')+1],fixName)
                    if pm.menuItem('nodeRenameDiagnostics',q=1,checkBox=1):
                        print "̰���󷨣�%s to ��%s  output: %s" % (str(rule),str(fixName),str(inputName))
                newName = inputName
                if '*' in inputName and ',' not in inputName and '.' not in inputName and '-' not in inputName and '|' not in inputName or a in inputName and  ',' not in inputName and '.' not in inputName and '-' not in inputName and '|' not in inputName or b in inputName and  ',' not in inputName and '.' not in inputName and '-' not in inputName and '|' not in inputName:
                    #if '.' not in inputName and '-' not in inputName and '|' not in inputName:
                    newName = inputName.replace('*',str(oldShortName)).replace(a,str(n)).replace(b,str(x))
                    if pm.menuItem('nodeRenameDiagnostics',q=1,checkBox=1):
                        print "���������:%s" % str(newName)  
        #�滻�� ֧��̰����
                elif ',' in inputName and '.' not in inputName and '|' not in inputName:
                    if pm.menuItem('nodeRenameDiagnostics',q=1,checkBox=1):
                        if pm.menuItem('nodeRenameDiagnostics',q=1,checkBox=1):
                            print "���붺����,�滻��:"
                    fixOne = inputName.split(',')[0]
                    fixTow = inputName.split(',')[1]
                    if '*' in fixOne:
                        fixOne = fixOne.replace('*','\w+')
                    try:
                        fixName = re.findall(fixOne,oldShortName)[0]
                    except:
                        fixName = fixOne                    
                        if '-' in fixOne[0]:
                            c = fixOne.split('-')[-1]
                            if self.isInt(c):
                                #print self.isInt(c)
                                try:
                                    fixName = oldShortName.split('_')[int(c)]+'_'
                                    #print len(oldShortName.split('_'))
                                    if len(oldShortName.split('_'))-1 == int(c):
                                        fixName = oldShortName.split('_')[int(c)]
                                    #print fixName
                                except:
                                    print "%s:����ڵ�ֻ��%s��,�������滻��%d�Σ������ֶ���" % ( str(oldShortName),str(len(oldShortName.split('_'))),int(fixOne.split('-')[-1]) )
                                    pass
                    if '*' in fixTow or a in fixTow or b in fixTow:
                        fixTow = fixTow.replace('*',str(oldShortName)).replace(a,str(n)).replace(b,str(x))
                    newName = oldShortName.replace(fixName,fixTow,1)
        #�������
                elif '-' in inputName and ',' not in inputName:
                    if pm.menuItem('nodeRenameDiagnostics',q=1,checkBox=1):
                        print "�������������:"
                    c = inputName.split('-')[-1]
                    if self.isInt(c):
                        try:
                            newName = oldShortName.replace(oldShortName.split('_')[int(inputName.split('-')[-1])] +'_','',1)
                            if len(oldShortName.split('_'))-1 == int(c):
                                newName = oldShortName.replace(oldShortName.split('_')[int(inputName.split('-')[-1])],'',1)
                            if pm.menuItem('nodeRenameDiagnostics',q=1,checkBox=1):        
                                print newName
                        except:	
                            print "%s:����ڵ�ֻ��%s��,������ɾ����%d�Σ������ֶ���" % ( str(oldShortName),str(len(oldShortName.split('_'))),int(inputName.split('-')[-1])-1 )
                            pass
                    elif '->' in inputName:
                        newName = oldShortName[1:]#.replace(oldShortName[0],'',1)
                    elif '<-' in inputName:
                        newName = oldShortName[0:-1]#.replace(oldShortName[-1],'',1)
                    elif '-:' in inputName:
                        if len(s.namespace())>0:
                            print ("�Ƴ����ֿռ䣺" +str(s.namespace()))
                            newName = oldShortName.split(':')[-1]
                        else:
                            print "%s : ����ڵ�û�����ֿռ�" % str(s)
                            continue
                    else:                        
                        newName = oldShortName.replace(inputName.split('-')[-1],'',1)
                elif '.' in inputName[0] and '-' not in inputName and '|' not in inputName:
                    if pm.menuItem('nodeRenameDiagnostics',q=1,checkBox=1):
                        print "���뺯�������ַ�����"
                    try:
                        newName = eval('oldShortName' + inputName)
                    except:
                        print "%s :��ʽ���󣬿����Ҽ��鿴��" % inputName
                        break
        #�Ӽ�����
                elif '|' in inputName[0] and '.' not in inputName and '-' not in inputName:
                    if pm.menuItem('nodeRenameDiagnostics',q=1,checkBox=1):
                        print "�����Ӽ�������"
                    try:
                        if isinstance( s, pm.nodetypes.DagNode) and isinstance(s.getChildren()[0], pm.nodetypes.Shape)==0:
                            print "������������ʼ��"
                            newName = inputName.split('|')[-1].replace('$','').replace('#','')
                            if '*' in inputName:
                                newName = newName.replace(a,'').replace(b,'').replace('*',str(oldShortName))
                            newName = oldLongName.replace(oldShortName,newName)
                            newNode  = pm.rename(s,newName)
                            try:
                                if newName+'Shape' not in newNode.getShape().longName():
                                    print ('shape�ڵ㲻���Ϲ���: %s to : %s �Ѹ���') %(str(newNode.getShape()),str(newName+'Shape'))
                                    shapeNode = pm.rename(newNode.getShape(),newName+'Shape')
                            except:
                                pass            
                            children = newNode.getChildren()
                            #print children
                            if len(children)>0:
                                i=97
                                n=1
                                for ss in children:
                                    childrenSort = ''
                                    x = chr(i)
                                    if a in inputName:
                                        childrenSort +=  str(n)
                                    if b in inputName:
                                        childrenSort += str(x)
                                    childrenNewNode = pm.rename(ss,s+'_' + childrenSort)
                                    print "%s to : %s finish!" % (str(ss),str(childrenNewNode))
                                    try:
                                        if childrenNewNode+'Shape' not in childrenNewNode.getShape().longName():
                                            print ('�Ӽ���shape�ڵ㲻���Ϲ���: %s to : %s �Ѹ���') %(str(childrenNewNode.getShape()),str(childrenNewNode+'Shape'))
                                            shapeNode = pm.rename(childrenNewNode.getShape(),childrenNewNode+'Shape')
                                    except:
                                        pass    
                                    n+=1
                                    i+=1
                                    if i > 122:
                                        i=65
                            else:
                                print "%s : ����ڵ�û��������1��" % str(s)
                                newName = oldShortName
                    except:
                        print "%s : ����ڵ�û��������2��" % str(s)
                        break
                if '<type>' in newName:
                    if pm.menuItem('nodeRenameDiagnostics',q=1,checkBox=1):
                        print "̰����׺�󷨣�"
                    if s.type() == "transform":
                        try:
                            typeName = typeDict[s.getShape().type()]
                        except:
                            typeName = typeDict['group']
                    else:
                        try:
                            typeName = typeDict[s.type()]
                        except:
                            typeName = '_' + s.type()
                    if s.name()[int(-len(typeName)):-1]+s.name()[-1:] != typeName:
                        newName = newName.replace('<type>',typeName)
                    else:
                        newName = newName.replace('<type>','')

                    
            #��ʼִ������
                newName = oldLongName.replace(oldShortName,newName)
                if len(children) == 0:
                    try:
                        if str(newName).split('|')[-1] != str(s):
                            print  ('%s to : %s  �Ѹ���') % (str(s),str(newName))
                            newNode  = pm.rename(s,newName)
                        newNode = s
                        if isinstance(newNode,pm.nodetypes.DagNode):
                            try:
                                if newName.split('|')[-1]+'Shape' not in newNode.getShape().longName():
                                    print ('shape�ڵ㲻���Ϲ���: %s to : %s �Ѹ���') %(str(newNode.getShape()),str(newName.split('|')[-1]+'Shape'))
                                    shapeNode = pm.rename(newNode.getShape(),newName+'Shape')
                            except:
                                pass
                        else:
                            try:
                                #path = self._nodeTypePath
                                if newNode.type() in typeDict:
                                    if typeDict[newNode.type()] == '_mat':
                                        if str(newNode.shadingGroups()[0])!=str(newNode)+"SG":
                                            print "��鵽����ڵ���shader�������Զ��޸�SG�ڵ㣬%s to: %s" % (str(newNode.shadingGroups()[0]),str(newNode)+"SG")
                                            pm.rename(newNode.shadingGroups()[0],newNode+"SG")
                            except:
                                print "�ֵ����"
                                pass
                    except:
                        print "%s :�ýڵ㲻�ܸ������ʽ����" % str(s)
                        pass                    
				#����
                n+=1
                i+=1
                if i > 122:
                    i=65
                if 90<i <97:
                    #print "��ѡ�е�file�ڵ�̫�࣬��$���ܳ���52��,�����Ĳ������������ֱ�ʾ����0��ʼ����!"
                    i=48

        else:
            print "��ѡ��һ������Node��"
            
    def renmaeCMD(self,*args):
        getTex = pm.textField("nodeRenameTexField",q=1,tx=1)        
        self.renmaeNode(getTex)
    def removeLastOne(self,*args):
        self.renmaeNode("<-")
    def removeFirstOne(self,*args):
        self.renmaeNode("->")
    def fixhape(self,*args):
        self.renmaeNode("*")
    def autoType(self,*args):
        self.renmaeNode("*<type>")
        
    def UI(self):
        if pm.window('nodeRename', exists=True):
            pm.deleteUI('nodeRename', window=True)
        pm.window( 'nodeRename',widthHeight=(232, 30),s=0)
        buttonColor1 = (0.6,0.6,0.55)
        buttonColor2 = (0.65,0.65,0.55)
        pm.rowColumnLayout( numberOfColumns=2,h = 30,columnWidth=[(1, 150), (2, 80), (3, 80)])
        pm.textField('nodeRenameTexField',tx='*')
        pm.popupMenu()
        pm.menuItem( divider=True, l='�����������' ,bld=0)
        pm.menuItem( divider=True, l='    ����' )
        pm.menuItem(l='    ����ԭʼ��   :     *',c= 'pm.textField("nodeRenameTexField",e=1,tx="*")' ,bld=0)
        pm.menuItem(l='    ��ǰ׺           :     abcd_*',c= 'pm.textField("nodeRenameTexField",e=1,tx="abcd_*")',bld=1 )
        pm.menuItem(l='    �Ӻ�׺           :     *_abcd',c= 'pm.textField("nodeRenameTexField",e=1,tx="*_abcd")' ,bld=1)
        pm.menuItem(l='    �����ͺ�׺   :     *<type>',c= 'pm.textField("nodeRenameTexField",e=1,tx="*<type>")' ,bld=1)
        pm.menuItem(l='    �滻����       :     abcd,ABCD',c= 'pm.textField("nodeRenameTexField",e=1,tx="abcd,ABCD")' ,bld=1)
        pm.menuItem( subMenu=True, label='ģ�ͳ��ú�׺' )
        pm.menuItem(l='    ��ģ�ͺ�׺    :     *_mdl',c= 'pm.textField("nodeRenameTexField",e=1,tx="*_mdl")' )
        pm.menuItem(l='    �����׺       :      *_grp',c= 'pm.textField("nodeRenameTexField",e=1,tx="*_grp")' )
        pm.setParent( '..', menu=True )
        pm.menuItem( subMenu=True, label='���ʳ��ú�׺' )
        pm.menuItem(l='    ��shader��׺:     *_mat',c= 'pm.textField("nodeRenameTexField",e=1,tx="*_mat")' )
        pm.menuItem(l='    ��SG��׺:     *SG',c= 'pm.textField("nodeRenameTexField",e=1,tx="*SG")' )
        pm.menuItem(l='    ��file��׺:     *_file',c= 'pm.textField("nodeRenameTexField",e=1,tx="*_file")' )
        pm.menuItem(l='    ��filetextureplace2d��׺:     *_p2d',c= 'pm.textField("nodeRenameTexField",e=1,tx="*_p2d")' )
        pm.menuItem(l='    ��bump��׺:     *bp',c= 'pm.textField("nodeRenameTexField",e=1,tx="*SG")' )
        pm.setParent( '..', menu=True )
        pm.menuItem( subMenu=True, label='�ƹⳣ�ú�׺' )
        pm.menuItem(l='    ��light��׺:     *_lit',c= 'pm.textField("nodeRenameTexField",e=1,tx="*_lit")' )
        pm.menuItem(l='    ��renderLayer��׺:     *_RL',c= 'pm.textField("nodeRenameTexField",e=1,tx="*_RL")' )
        pm.setParent( '..', menu=True )
        pm.menuItem( divider=True, l='    ����' )
        pm.menuItem(l='    �����ֱ��(1-n)       :     *# ',c= 'pm.textField("nodeRenameTexField",e=1,tx="*#")',bld=0 )
        pm.menuItem(l='    ����ĸ���(a-z,A-Z) :     *$ ',c= 'pm.textField("nodeRenameTexField",e=1,tx="*$")' ,bld=0)
        pm.menuItem( divider=True, l='    ������ʽ̰����' )
        pm.menuItem( divider=True, l='        ��Ӧ�����������滻����ʹ��' )
        pm.menuItem(l='    ���a��c֮����ַ�  :     [a*c]',c= 'pm.textField("nodeRenameTexField",e=1,tx="[a*c]")' )
        pm.menuItem(l='    ��ôӵ�һ����ĸ��c֮����ַ�  :     [*c]',c= 'pm.textField("nodeRenameTexField",e=1,tx="[*c]")' )
        pm.menuItem(l='    ��ô�c��ʼ�������ַ�  :     [c*]',c= 'pm.textField("nodeRenameTexField",e=1,tx="[c*]")' )
        pm.menuItem(l='    ��ôӵ�0��4֮����ַ�  :     [0:4]',c= 'pm.textField("nodeRenameTexField",e=1,tx="[0:4]")' )
        pm.menuItem(l='    ��ô�ĳλ������4λ֮����ַ�  :     [-1:4]',c= 'pm.textField("nodeRenameTexField",e=1,tx="[-1:4]")' )
        pm.menuItem(l='    ������ֲ��޳�  :     [\d+],',c= 'pm.textField("nodeRenameTexField",e=1,tx="[\d+],")' )
        pm.menuItem( divider=True, l='    �����ʽ' )
        pm.menuItem(l='    ɾ��"_"�ֶα�ŵ�0��  :     -0',c= 'pm.textField("nodeRenameTexField",e=1,tx="-0")' )
        pm.menuItem(l='    �滻"_"�ֶα�ŵ�0��  :     -0,abc',c= 'pm.textField("nodeRenameTexField",e=1,tx="-0,abc")' )
        pm.menuItem(l='    ɾ������                     :     ->',c= 'pm.textField("nodeRenameTexField",e=1,tx="->")' )
        pm.menuItem(l='    ɾ��β��                     :     <-',c= 'pm.textField("nodeRenameTexField",e=1,tx="<-")' )
        pm.menuItem(l='    ����ĸ��д                 :     .capitalize()',c= 'pm.textField("nodeRenameTexField",e=1,tx=".capitalize()")' )
        pm.menuItem(l='    ȫ����д                     :     .upper()',c= 'pm.textField("nodeRenameTexField",e=1,tx=".upper()")' )
        pm.menuItem(l='    ȫ��Сд                     :     .lower()',c= 'pm.textField("nodeRenameTexField",e=1,tx=".lower()")' )		
        pm.menuItem(l='    ȥ�����ֿռ�              :     -:',c= 'pm.textField("nodeRenameTexField",e=1,tx="-:")' )
        pm.menuItem('nodeRenameDiagnostics',l=' ���ģʽ(nodeRenameDiagnostics)',checkBox=False)
        pm.menuItem(l='��ȡѡ�е�һ��������',c= 'pm.textField("nodeRenameTexField",e=1,tx=pm.ls(sl=1)[0].split("|")[-1])',bld=1)
        pm.menuItem(l='��ȡѡ�����һ��������',c= 'pm.textField("nodeRenameTexField",e=1,tx=pm.ls(sl=1)[-1].split("|")[-1])',bld=1)
        pm.button(l="rename",c=self.renmaeCMD,bgc = (random.uniform(0.1,1),random.uniform(0.1,1),random.uniform(0.1,1)),ann = "����������\"*\"                 ����ԭʼ����;\n	     \"#\"                �������ֱ��;\n	     \"abcd,ABCD\"����abcd�滻��ABCD,��\",\"����;\n	     \"abcd, \"         ����ȥ��\",\"ǰ������")
        pm.popupMenu(markingMenu =1)
        pm.menuItem(l='ɾ��β��:<-',radialPosition = 'E',c=self.removeLastOne)
        pm.menuItem(l='ɾ������:->',radialPosition = 'W',c=self.removeFirstOne)
        pm.menuItem(l='�޸�shape�ڵ�:*',radialPosition = 'N',c=self.fixhape)
        pm.menuItem(l='̰����׺:*<type>',radialPosition = 'S',c=self.autoType)
        pm.menuItem(l='ѡ������mesh',c='pm.select(pm.ls(type="mesh")),pm.pickWalk(d="up")')
        
        pm.showWindow('nodeRename')