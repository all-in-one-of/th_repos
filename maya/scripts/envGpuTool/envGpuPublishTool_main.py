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

import glob
import logging
from PySide import QtGui,QtCore
# Third-party modules
import yaml
try:
    import pymel.core as pm
    import maya.OpenMaya as om
    import maya.OpenMayaUI as omUI
    import shiboken
except:
    pass
import cgtk_qt

import jarryLibs
import zkLibs

__CURRENT_FILE__ = os.path.dirname(__file__)

Ui_UI,ui_Dialog = cgtk_qt.load_ui_type('%s/gpuPublishGUI.ui'%__CURRENT_FILE__)
#gpuUIV
        
def getMayaWindow():
#    'Get the maya main window as a QMainWindow instance'
    ptr = omUI.MQtUtil.mainWindow()
    if ptr is not None:    
        return shiboken.wrapInstance(long(ptr), QtGui.QMainWindow)
       
        
class gpuPublish_mainUI(ui_Dialog, Ui_UI):
    def __init__(self,parent = None):
        super(gpuPublish_mainUI,self).__init__(parent)
        
        self.setupUi(self)
        
        #设置标题栏有最大化
        #self.setWindowFlags(QtCore.Qt.WindowMaximizeButtonHint)
        #设置窗口始终处于顶层
        #self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        #-----------------
        #qss美化UI
        #不显示标题栏
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Dialog)
        self.setStyleSheet("* {font-family:'黑体';color: rgb(200, 200, 200);} \
                           QMainWindow#envGpuPublishToolUI{background-color: rgb(50, 50, 50);selection-background-color: rgb(50, 80, 139);}")
                
        #设置图标        
        title_icon_path = '%s/icon/out_gpuCache.png'%__CURRENT_FILE__  
        gpuSLoad_icon_path = '%s/icon/gpuSLoad_icon.png'%__CURRENT_FILE__
        gpuPLoad_icon_path = '%s/icon/gpuPLoad_icon.png'%__CURRENT_FILE__
        gpu2abc_icon_path = '%s/icon/communication.png'%__CURRENT_FILE__
        self.setWindowIcon(QtGui.QIcon(title_icon_path))
        self.titleIconLab.setPixmap(QtGui.QPixmap(title_icon_path))
        
        self.snapshot_label.setSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)   
        self.snapshot_label.setScaledContents(True) 
        
       #-------------------
        #Signal
        self.refresh_PB.clicked.connect(self.setInfo)
        self.capture_pb.clicked.connect(self.capture)
        self.publish_pb.clicked.connect(self.publishGpu)
        
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)

    def setInfo(self):        

        currentSceneName = pm.sceneName()
        if currentSceneName:
            assetPath,assetName,assetVer = zkLibs.getAssetInfoFromFile(currentSceneName)
        elif not currentSceneName:
            assetPath,assetName,assetVer = '','',''
        
        if assetName:
            self.assetName_LineEdit.setText(assetName)
            self.assetName_LineEdit.setStyleSheet('selection-background-color: rgb(0, 170, 0);')
            assetCHName = zkLibs.get_assets_CHName(assetName)
            if assetCHName:
                self.assetCHName_LineEdit.setText(assetCHName)
                self.assetCHName_LineEdit.setStyleSheet('selection-background-color: rgb(150, 40,40);')
            else:
                #self.assetCHName_LineEdit.setText(u'未检测到资产中文名')
                self.assetCHName_LineEdit.setStyleSheet('background-color: rgb(100,0,0);selection-background-color: rgb(150, 40,40);')
                logging.info(u'未查询到资产对应资产中文名，请检联系制片是否录入！')
                
        else:
            #self.assetName_LineEdit.setText(u'未查询到资产名称')
            self.assetName_LineEdit.setStyleSheet('background-color: rgb(100,0,0);selection-background-color: rgb(0, 170, 0);')
            logging.info(u'未查询到资产名称，请检查你的文件命名格式是否为规范！')
            
        if assetVer:
            self.assetVersion_LineEdit.setText(assetVer)
            self.assetVersion_LineEdit.setStyleSheet('selection-background-color: rgb(255, 85, 0);')
        else:
            #self.assetVersion_LineEdit.setText(u'未查询到资产对应版本号')
            self.assetVersion_LineEdit.setStyleSheet('background-color: rgb(100,0,0);selection-background-color: rgb(255, 85, 0);')
            logging.info(u'未查询到资产对应版本号，请检查你的文件命名格式是否为规范！')
        self.snapshot_label.setText(u'     点击按钮抓屏显示,publish后会将图片存储对应位置!' )
        
        self.refreshPathLineE()
    def getDeclaration(self):
        text = self.textEdit.toPlainText()
        return text
        
    def refreshPathLineE(self):
        assetName = self.assetName_LineEdit.text()
        setp = self.assetStep_LineEdit.text()
        ver = self.assetVersion_LineEdit.text()
        if assetName and setp and ver:
            publishPath,publishFileFormat = zkLibs.get_assets_file_path(assetName,'Publish',setp,ver,'%s')            
            self.publishPath_LineEdit.setText(os.path.join(publishPath,ver))
        else:
            self.publishPath_LineEdit.setText('')
            
    def publishGpu(self):
        assetName = self.assetName_LineEdit.text()
        setp = self.assetStep_LineEdit.text()
        ver = self.assetVersion_LineEdit.text()
        if assetName and setp and ver:
            publishPath,publishFileFormat = zkLibs.get_assets_file_path(assetName,'Publish',setp,ver,'%s')
            dec = self.getDeclaration()
            pixmap = self.snapshot_label.pixmap()
            if dec:
                if pixmap:
                
                    assetPath = os.path.join(publishPath,ver)
                    gpuFile = publishFileFormat%'abc'
                    ymlFile = publishFileFormat%'yml'                
                    imageFile = publishFileFormat%'jpg'
                    
                    findFile = glob.glob('%s/%s'%(assetPath,gpuFile))
                    
                    if findFile and self.forceVersion_cb.isChecked() or not findFile:                    
                        if not self.onlySnapshot_cb.isChecked():
                            import write_gpuCache as wgpu
                            reload(wgpu)
                            if wgpu.write_gpuCache(assetPath,assetName,gpuFile.replace('.abc',''),ymlFile,dec):
                                logging.info(u'Publish:%s'%os.path.join(assetPath,gpuFile))
                        
                        imagePath = os.path.join(assetPath,imageFile)
                        if pixmap.save(imagePath):
                            logging.info(u'publish:%s'%imagePath)
                        
                    else:
                        logging.info(u'已经存在这个版本了，想继续publish，请勾选强制覆盖已存在版本！')
                else:
                    logging.info(u'请获快照截屏后再publish！')
            else:
                logging.info(u'请获输入资产描述信息后再publish！')
        else:
            logging.info(u'请获取到正确的信息后再publish！')

    def capture(self):
        self.snapshot = jarryLibs.captureSnapshot()
        pixmap = self.snapshot.capture()
        #self.pixmap = self.snapshot.capturePlayblast()
        self.snapshot_label.setPixmap(pixmap )
        
        

def run(dock=False):
    name = 'envGpuPublishToolUI'
    if pm.window(name, q=1, ex=1):
        pm.deleteUI(name)
    ui = gpuPublish_mainUI(parent=getMayaWindow())
    
    if not dock:
        ui.show()
    else:
        dockName = 'envGpuPublishTool'

        if pm.dockControl(dockName, q=1, ex=1):
            pm.deleteUI(dockName)


        pm.dockControl(dockName, area='right',
                     content = ui.objectName(),
                     width=370,
                     label=ui.objectName(),
                     allowedArea=['right', 'left'])
                     
if __name__ == "__main__":    
    pass
    #app=QtGui.QApplication(sys.argv)  
    #my_ui = gpuPublish_mainUI()   
    
    #my_ui.show()
    #app.exec_()    
    
        
        


