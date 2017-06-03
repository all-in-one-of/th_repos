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
        将导出的json数据导入进来
        Args:
            path: 字符串,json数据文件的完整的路径

        Returns:
            返回json文件内的数据
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
            print "请选中一个或多个shader！"
            
    def addMat(self):
        selectList = pm.ls(sl=1)
        if len(selectList)>0:
            for s in self.selectList:
                if '_mat' not in str(s):
                    pm.rename(s,s+"_mat")
        else:
            print "请选中一个或多个shader！"
			
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
            print "没有json文件"
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
        #正则表达式 贪婪大法
                if '[' in inputName and ']' in inputName:
                    rule = inputName[inputName.find('[')+1:inputName.find(']')].replace('*','\w+')                        
                    if ':' not in rule:
                        try:
                            fixName = re.findall(rule,oldShortName)[0]
                        except:
                            print "正则表达式格式输入错误,请查看帮助！"
                            break
                    elif ':' in rule:          
                        fixName = eval('oldShortName' + '['+rule+']')
                    inputName = inputName.replace(inputName[inputName.find('['):inputName.find(']')+1],fixName)
                    if pm.menuItem('nodeRenameDiagnostics',q=1,checkBox=1):
                        print "贪婪大法：%s to ：%s  output: %s" % (str(rule),str(fixName),str(inputName))
                newName = inputName
                if '*' in inputName and ',' not in inputName and '.' not in inputName and '-' not in inputName and '|' not in inputName or a in inputName and  ',' not in inputName and '.' not in inputName and '-' not in inputName and '|' not in inputName or b in inputName and  ',' not in inputName and '.' not in inputName and '-' not in inputName and '|' not in inputName:
                    #if '.' not in inputName and '-' not in inputName and '|' not in inputName:
                    newName = inputName.replace('*',str(oldShortName)).replace(a,str(n)).replace(b,str(x))
                    if pm.menuItem('nodeRenameDiagnostics',q=1,checkBox=1):
                        print "进入基础类:%s" % str(newName)  
        #替换大法 支持贪婪大法
                elif ',' in inputName and '.' not in inputName and '|' not in inputName:
                    if pm.menuItem('nodeRenameDiagnostics',q=1,checkBox=1):
                        if pm.menuItem('nodeRenameDiagnostics',q=1,checkBox=1):
                            print "进入逗号类,替换大法:"
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
                                    print "%s:这个节点只有%s段,但你想替换第%d段，超过分段数" % ( str(oldShortName),str(len(oldShortName.split('_'))),int(fixOne.split('-')[-1]) )
                                    pass
                    if '*' in fixTow or a in fixTow or b in fixTow:
                        fixTow = fixTow.replace('*',str(oldShortName)).replace(a,str(n)).replace(b,str(x))
                    newName = oldShortName.replace(fixName,fixTow,1)
        #特殊符号
                elif '-' in inputName and ',' not in inputName:
                    if pm.menuItem('nodeRenameDiagnostics',q=1,checkBox=1):
                        print "进入特殊符号类:"
                    c = inputName.split('-')[-1]
                    if self.isInt(c):
                        try:
                            newName = oldShortName.replace(oldShortName.split('_')[int(inputName.split('-')[-1])] +'_','',1)
                            if len(oldShortName.split('_'))-1 == int(c):
                                newName = oldShortName.replace(oldShortName.split('_')[int(inputName.split('-')[-1])],'',1)
                            if pm.menuItem('nodeRenameDiagnostics',q=1,checkBox=1):        
                                print newName
                        except:	
                            print "%s:这个节点只有%s段,但你想删除第%d段，超过分段数" % ( str(oldShortName),str(len(oldShortName.split('_'))),int(inputName.split('-')[-1])-1 )
                            pass
                    elif '->' in inputName:
                        newName = oldShortName[1:]#.replace(oldShortName[0],'',1)
                    elif '<-' in inputName:
                        newName = oldShortName[0:-1]#.replace(oldShortName[-1],'',1)
                    elif '-:' in inputName:
                        if len(s.namespace())>0:
                            print ("移除名字空间：" +str(s.namespace()))
                            newName = oldShortName.split(':')[-1]
                        else:
                            print "%s : 这个节点没有名字空间" % str(s)
                            continue
                    else:                        
                        newName = oldShortName.replace(inputName.split('-')[-1],'',1)
                elif '.' in inputName[0] and '-' not in inputName and '|' not in inputName:
                    if pm.menuItem('nodeRenameDiagnostics',q=1,checkBox=1):
                        print "进入函数处理字符串类"
                    try:
                        newName = eval('oldShortName' + inputName)
                    except:
                        print "%s :格式错误，可以右键查看！" % inputName
                        break
        #子级控制
                elif '|' in inputName[0] and '.' not in inputName and '-' not in inputName:
                    if pm.menuItem('nodeRenameDiagnostics',q=1,checkBox=1):
                        print "进入子级控制类"
                    try:
                        if isinstance( s, pm.nodetypes.DagNode) and isinstance(s.getChildren()[0], pm.nodetypes.Shape)==0:
                            print "子物体命名开始："
                            newName = inputName.split('|')[-1].replace('$','').replace('#','')
                            if '*' in inputName:
                                newName = newName.replace(a,'').replace(b,'').replace('*',str(oldShortName))
                            newName = oldLongName.replace(oldShortName,newName)
                            newNode  = pm.rename(s,newName)
                            try:
                                if newName+'Shape' not in newNode.getShape().longName():
                                    print ('shape节点不符合规则: %s to : %s 已改名') %(str(newNode.getShape()),str(newName+'Shape'))
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
                                            print ('子级里shape节点不符合规则: %s to : %s 已改名') %(str(childrenNewNode.getShape()),str(childrenNewNode+'Shape'))
                                            shapeNode = pm.rename(childrenNewNode.getShape(),childrenNewNode+'Shape')
                                    except:
                                        pass    
                                    n+=1
                                    i+=1
                                    if i > 122:
                                        i=65
                            else:
                                print "%s : 这个节点没有子物体1！" % str(s)
                                newName = oldShortName
                    except:
                        print "%s : 这个节点没有子物体2！" % str(s)
                        break
                if '<type>' in newName:
                    if pm.menuItem('nodeRenameDiagnostics',q=1,checkBox=1):
                        print "贪婪后缀大法："
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

                    
            #开始执行命名
                newName = oldLongName.replace(oldShortName,newName)
                if len(children) == 0:
                    try:
                        if str(newName).split('|')[-1] != str(s):
                            print  ('%s to : %s  已改名') % (str(s),str(newName))
                            newNode  = pm.rename(s,newName)
                        newNode = s
                        if isinstance(newNode,pm.nodetypes.DagNode):
                            try:
                                if newName.split('|')[-1]+'Shape' not in newNode.getShape().longName():
                                    print ('shape节点不符合规则: %s to : %s 已改名') %(str(newNode.getShape()),str(newName.split('|')[-1]+'Shape'))
                                    shapeNode = pm.rename(newNode.getShape(),newName+'Shape')
                            except:
                                pass
                        else:
                            try:
                                #path = self._nodeTypePath
                                if newNode.type() in typeDict:
                                    if typeDict[newNode.type()] == '_mat':
                                        if str(newNode.shadingGroups()[0])!=str(newNode)+"SG":
                                            print "检查到这个节点是shader，帮你自动修改SG节点，%s to: %s" % (str(newNode.shadingGroups()[0]),str(newNode)+"SG")
                                            pm.rename(newNode.shadingGroups()[0],newNode+"SG")
                            except:
                                print "字典出错！"
                                pass
                    except:
                        print "%s :该节点不能改名或格式错误！" % str(s)
                        pass                    
				#排序
                n+=1
                i+=1
                if i > 122:
                    i=65
                if 90<i <97:
                    #print "你选中的file节点太多，用$不能超过52个,超过的部分现在用数字表示，从0开始算起!"
                    i=48

        else:
            print "请选中一个或多个Node！"
            
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
        pm.menuItem( divider=True, l='输入规则快捷栏' ,bld=0)
        pm.menuItem( divider=True, l='    常用' )
        pm.menuItem(l='    插入原始名   :     *',c= 'pm.textField("nodeRenameTexField",e=1,tx="*")' ,bld=0)
        pm.menuItem(l='    加前缀           :     abcd_*',c= 'pm.textField("nodeRenameTexField",e=1,tx="abcd_*")',bld=1 )
        pm.menuItem(l='    加后缀           :     *_abcd',c= 'pm.textField("nodeRenameTexField",e=1,tx="*_abcd")' ,bld=1)
        pm.menuItem(l='    加类型后缀   :     *<type>',c= 'pm.textField("nodeRenameTexField",e=1,tx="*<type>")' ,bld=1)
        pm.menuItem(l='    替换名字       :     abcd,ABCD',c= 'pm.textField("nodeRenameTexField",e=1,tx="abcd,ABCD")' ,bld=1)
        pm.menuItem( subMenu=True, label='模型常用后缀' )
        pm.menuItem(l='    加模型后缀    :     *_mdl',c= 'pm.textField("nodeRenameTexField",e=1,tx="*_mdl")' )
        pm.menuItem(l='    加组后缀       :      *_grp',c= 'pm.textField("nodeRenameTexField",e=1,tx="*_grp")' )
        pm.setParent( '..', menu=True )
        pm.menuItem( subMenu=True, label='材质常用后缀' )
        pm.menuItem(l='    加shader后缀:     *_mat',c= 'pm.textField("nodeRenameTexField",e=1,tx="*_mat")' )
        pm.menuItem(l='    加SG后缀:     *SG',c= 'pm.textField("nodeRenameTexField",e=1,tx="*SG")' )
        pm.menuItem(l='    加file后缀:     *_file',c= 'pm.textField("nodeRenameTexField",e=1,tx="*_file")' )
        pm.menuItem(l='    加filetextureplace2d后缀:     *_p2d',c= 'pm.textField("nodeRenameTexField",e=1,tx="*_p2d")' )
        pm.menuItem(l='    加bump后缀:     *bp',c= 'pm.textField("nodeRenameTexField",e=1,tx="*SG")' )
        pm.setParent( '..', menu=True )
        pm.menuItem( subMenu=True, label='灯光常用后缀' )
        pm.menuItem(l='    加light后缀:     *_lit',c= 'pm.textField("nodeRenameTexField",e=1,tx="*_lit")' )
        pm.menuItem(l='    加renderLayer后缀:     *_RL',c= 'pm.textField("nodeRenameTexField",e=1,tx="*_RL")' )
        pm.setParent( '..', menu=True )
        pm.menuItem( divider=True, l='    排序' )
        pm.menuItem(l='    加数字编号(1-n)       :     *# ',c= 'pm.textField("nodeRenameTexField",e=1,tx="*#")',bld=0 )
        pm.menuItem(l='    加字母编号(a-z,A-Z) :     *$ ',c= 'pm.textField("nodeRenameTexField",e=1,tx="*$")' ,bld=0)
        pm.menuItem( divider=True, l='    正则表达式贪婪大法' )
        pm.menuItem( divider=True, l='        可应用于命名和替换叠加使用' )
        pm.menuItem(l='    获得a到c之间的字符  :     [a*c]',c= 'pm.textField("nodeRenameTexField",e=1,tx="[a*c]")' )
        pm.menuItem(l='    获得从第一个字母到c之间的字符  :     [*c]',c= 'pm.textField("nodeRenameTexField",e=1,tx="[*c]")' )
        pm.menuItem(l='    获得从c开始到最后的字符  :     [c*]',c= 'pm.textField("nodeRenameTexField",e=1,tx="[c*]")' )
        pm.menuItem(l='    获得从第0到4之间的字符  :     [0:4]',c= 'pm.textField("nodeRenameTexField",e=1,tx="[0:4]")' )
        pm.menuItem(l='    获得从某位倒数第4位之间的字符  :     [-1:4]',c= 'pm.textField("nodeRenameTexField",e=1,tx="[-1:4]")' )
        pm.menuItem(l='    获得数字并剔除  :     [\d+],',c= 'pm.textField("nodeRenameTexField",e=1,tx="[\d+],")' )
        pm.menuItem( divider=True, l='    特殊格式' )
        pm.menuItem(l='    删除"_"分段编号第0段  :     -0',c= 'pm.textField("nodeRenameTexField",e=1,tx="-0")' )
        pm.menuItem(l='    替换"_"分段编号第0段  :     -0,abc',c= 'pm.textField("nodeRenameTexField",e=1,tx="-0,abc")' )
        pm.menuItem(l='    删除首字                     :     ->',c= 'pm.textField("nodeRenameTexField",e=1,tx="->")' )
        pm.menuItem(l='    删除尾字                     :     <-',c= 'pm.textField("nodeRenameTexField",e=1,tx="<-")' )
        pm.menuItem(l='    首字母大写                 :     .capitalize()',c= 'pm.textField("nodeRenameTexField",e=1,tx=".capitalize()")' )
        pm.menuItem(l='    全部大写                     :     .upper()',c= 'pm.textField("nodeRenameTexField",e=1,tx=".upper()")' )
        pm.menuItem(l='    全部小写                     :     .lower()',c= 'pm.textField("nodeRenameTexField",e=1,tx=".lower()")' )		
        pm.menuItem(l='    去除名字空间              :     -:',c= 'pm.textField("nodeRenameTexField",e=1,tx="-:")' )
        pm.menuItem('nodeRenameDiagnostics',l=' 诊断模式(nodeRenameDiagnostics)',checkBox=False)
        pm.menuItem(l='获取选中第一个的名字',c= 'pm.textField("nodeRenameTexField",e=1,tx=pm.ls(sl=1)[0].split("|")[-1])',bld=1)
        pm.menuItem(l='获取选中最后一个的名字',c= 'pm.textField("nodeRenameTexField",e=1,tx=pm.ls(sl=1)[-1].split("|")[-1])',bld=1)
        pm.button(l="rename",c=self.renmaeCMD,bgc = (random.uniform(0.1,1),random.uniform(0.1,1),random.uniform(0.1,1)),ann = "批量改名：\"*\"                 代表原始名字;\n	     \"#\"                代表数字编号;\n	     \"abcd,ABCD\"代表abcd替换成ABCD,用\",\"区分;\n	     \"abcd, \"         代表去掉\",\"前的名字")
        pm.popupMenu(markingMenu =1)
        pm.menuItem(l='删除尾字:<-',radialPosition = 'E',c=self.removeLastOne)
        pm.menuItem(l='删除首字:->',radialPosition = 'W',c=self.removeFirstOne)
        pm.menuItem(l='修复shape节点:*',radialPosition = 'N',c=self.fixhape)
        pm.menuItem(l='贪婪后缀:*<type>',radialPosition = 'S',c=self.autoType)
        pm.menuItem(l='选中所有mesh',c='pm.select(pm.ls(type="mesh")),pm.pickWalk(d="up")')
        
        pm.showWindow('nodeRename')