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
import cgtk_qt
import jarryLibs
try:
    import pymel.core as pm
    import maya.OpenMaya as om
    import maya.OpenMayaUI as omUI
    import shiboken
except:
    pass
    
import load_gpuCache as lg
reload(lg)
import get_assets_gpuData as gpuData
reload(gpuData)

__CURRENT_FILE__ = os.path.dirname(__file__)

Ui_UI,ui_Dialog = cgtk_qt.load_ui_type('%s/gpuToolGUI.ui'%__CURRENT_FILE__)
#gpuUIV
def getMayaWindow():
#    'Get the maya main window as a QMainWindow instance'
    ptr = omUI.MQtUtil.mainWindow()
    if ptr is not None:    
        return shiboken.wrapInstance(long(ptr), QtGui.QMainWindow)

class ComboDelegate(QtGui.QItemDelegate):
    def __init__(self, parent):
        super(ComboDelegate, self).__init__(parent)
    def createEditor(self, parent, option, index):
        combo = QtGui.QComboBox(parent)
        #combo.setSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        #combo.setScaledContents(True)
        self.connect(combo, QtCore.SIGNAL("currentIndexChanged(int)"), self, QtCore.SLOT("currentIndexChanged()"))
        
        return combo
        
    def setEditorData(self, editor, index):
        model = index.model()
        data_index = model.index(index.row(), 4)
        getVerDict = model.data(data_index, QtCore.Qt.DisplayRole)
        if getVerDict:
            verDict = eval(getVerDict)
            if verDict:
                editor.clear()
                editor.addItems(verDict.keys())
        editor.blockSignals(True)
        currentText = model.data(model.index(index.row(), 3),QtCore.Qt.DisplayRole)
        editor.setCurrentIndex(verDict.keys().index(currentText))
        editor.blockSignals(False)
        
    def setModelData(self, editor, model, index):
        model.setData(model.index(index.row(),3), editor.currentText())
        #print self._verDict
        #model.setData(index, editor.currentText())
        data_index = model.index(index.row(), 4)
        getVerDict = model.data(data_index, QtCore.Qt.DisplayRole)
        if getVerDict:
            verDict = eval(getVerDict)
            currentText = model.data(model.index(index.row(), 3),QtCore.Qt.DisplayRole)
            preivewPath = verDict[currentText].replace('.yml','.jpg')
            if not os.path.isfile(preivewPath):
                preivewPath = ''
            data_index0 = model.index(index.row(), 0)    
            model.setData(data_index0,preivewPath)
            
    @QtCore.Slot()
    def currentIndexChanged(self):
        self.commitData.emit(self.sender())

class imageLabel(QtGui.QLabel):  
    def __init__(self,parent,index):  
        super(imageLabel,self).__init__(parent)  
        self.index = index

    def mouseDoubleClickEvent(self,e):  
        model = self.index.model()
        data_index = model.index(self.index.row(), 0)
        iamgePath = model.data(data_index, QtCore.Qt.DisplayRole)        
        os.popen(iamgePath)

        
class ReferenceImageDelegate(QtGui.QItemDelegate):
    def __init__(self, parent=None):
        super(ReferenceImageDelegate, self).__init__(parent)
        self._parent = parent
    def createEditor(self, parent, option, index):
        if index.column() == 0:
            label = imageLabel(parent,index)
            label.setSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
            label.setScaledContents(True)
            return label

    def setEditorData(self, editor, index):        
        model = index.model()
        data_index = model.index(index.row(), 0)
        value = model.data(data_index, QtCore.Qt.DisplayRole)
        if value:
            pix_map = QtGui.QPixmap(value)
            editor.setText(value)
            editor.setPixmap(pix_map)

class gpuAssets_FilterProxyModel(QtGui.QSortFilterProxyModel):
    def __init__(self, parent):        
        super(gpuAssets_FilterProxyModel, self).__init__(parent)
        self._parent = parent
        
        self.name_regexp = QtCore.QRegExp()
        self.chName_regexp = QtCore.QRegExp()
        self.inscene_regexp = QtCore.QRegExp()
        
        self.name_regexp.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.chName_regexp.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.inscene_regexp.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        
        self.name_regexp.setPatternSyntax(QtCore.QRegExp.RegExp)
        self.chName_regexp.setPatternSyntax(QtCore.QRegExp.RegExp)
        self.inscene_regexp.setPatternSyntax(QtCore.QRegExp.RegExp)
                
    def filterAcceptsRow(self, source_row, source_parent):
        name_index = self.sourceModel().index(source_row, 2, source_parent)
        chName_index = self.sourceModel().index(source_row, 1, source_parent)
        inscene_index = self.sourceModel().index(source_row, 5, source_parent)
        
        name = self.sourceModel().data(name_index)
        chName = self.sourceModel().data(chName_index)
        insceneName = self.sourceModel().data(inscene_index)
        
        if self.inscene_regexp.isEmpty():
            if self.name_regexp.isEmpty() and self.chName_regexp.isEmpty():
                return True                
            elif self.name_regexp.isEmpty() or self.chName_regexp.isEmpty():
                return self.name_regexp.exactMatch(name) or self.chName_regexp.exactMatch(chName)          
            else:
                return self.name_regexp.exactMatch(name) and self.chName_regexp.exactMatch(chName)
            
        else:             
            if self.name_regexp.isEmpty() and self.chName_regexp.isEmpty():
                return self.inscene_regexp.exactMatch(insceneName)                
            elif not self.name_regexp.isEmpty() and self.chName_regexp.isEmpty():
                return self.inscene_regexp.exactMatch(insceneName) and self.name_regexp.exactMatch(name)                
            elif not self.chName_regexp.isEmpty() and self.name_regexp.isEmpty():
                return self.inscene_regexp.exactMatch(insceneName) and self.chName_regexp.exactMatch(chName)            
            else:
                return self.name_regexp.exactMatch(name) and self.chName_regexp.exactMatch(chName) and self.inscene_regexp.exactMatch(insceneName)
                
            

    def set_name_filter(self, regexp):
        regexp = r".*%s.*" % regexp if regexp else ""
        self.name_regexp.setPattern(regexp)
        self.reset()
        self.rebuid()
            
    def set_chName_filter(self, regexp):
        regexp = r".*%s.*" % regexp if regexp else ""
        self.chName_regexp.setPattern(regexp)
        self.reset()
        self.rebuid()
    def set_inscene_filter(self, regexp):
        #regexp = r".*%s.*" % 'v002'#regexp if regexp else ""
        #self.inscene_regexp.setPattern('v002')
        #print type(regexp)
        if regexp == 2:
            self.inscene_regexp.setPattern('yes')
        else:
            self.inscene_regexp.setPattern('')
        self.reset()
        self.rebuid()
        
    def rebuid(self):
        for i in range(0,self.rowCount()):
            self._parent.setRowHeight(i,80)
            self._parent.openPersistentEditor(self.index(i,0))
            

        
class gpu_mainUI(ui_Dialog, Ui_UI):
    def __init__(self,parent =None):
        super(gpu_mainUI,self).__init__(parent)
        
        self.setupUi(self)
        
        #设置标题栏有最大化
        #self.setWindowFlags(QtCore.Qt.WindowMaximizeButtonHint)
        #设置窗口始终处于顶层
        #self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        
        self.splitter.setSizes([1, 0])
        #-----------------
        #qss美化UI
        #不显示标题栏
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Dialog)
        
        #qss加载
        file = QtCore.QFile('%s/style/gpuToolGUI_main.qss'%__CURRENT_FILE__)
        file.open(QtCore.QFile.ReadOnly)
        styleSheet = file.readAll()
        styleSheet = unicode(styleSheet, encoding='utf8')
        self.setStyleSheet(styleSheet)
                
        #设置图标        
        title_icon_path = '%s/icon/out_gpuCache.png'%__CURRENT_FILE__  
        gpuSLoad_icon_path = '%s/icon/gpuSLoad_icon.png'%__CURRENT_FILE__
        gpuPLoad_icon_path = '%s/icon/gpuPLoad_icon.png'%__CURRENT_FILE__
        gpu2abc_icon_path = '%s/icon/communication.png'%__CURRENT_FILE__
        self.setWindowIcon(QtGui.QIcon(title_icon_path))
        self.gpuSLoad_PB.setIcon(QtGui.QIcon(gpuSLoad_icon_path))
        self.gpuLoad_PB.setIcon(QtGui.QIcon(gpuPLoad_icon_path))
        self.gpu2abc_PB.setIcon(QtGui.QIcon(gpu2abc_icon_path))
        self.titleIconLab.setPixmap(QtGui.QPixmap(title_icon_path))
        #-----------
        #set model
        self.tableView = self.gpuTool_tableVw        
        self.model = QtGui.QStandardItemModel(self.tableView)
        self.proxy_model = gpuAssets_FilterProxyModel(self.tableView)                
        
        self.proxy_model.setSourceModel(self.model)
        self.tableView.setModel(self.proxy_model)        
        self.proxy_model.setDynamicSortFilter(True)
        self.proxy_model.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)
                
        self.setup_model()
       
       #-------------------
        #Signal
        self.gpuSearch_LineEdit.textChanged.connect(self.proxy_model.set_name_filter)
        self.gpuChSearch_LineEdit.textChanged.connect(self.proxy_model.set_chName_filter)
        self.inScence_cbox.stateChanged.connect(self.proxy_model.set_inscene_filter)
        self.getDecInfo_TB.clicked.connect(self.getDesc)
        self.gpu2abc_PB.clicked.connect(self.gpu2abc)
        #stateChanged 
        self.refresh_PB.clicked.connect(self.setup_model)
        
        self.gpuLoad_PB.clicked.connect(self.load_gpu)
        self.gpuSLoad_PB.clicked.connect(self.load_single_gpu)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)

    def setup_model(self):  
        self.loadGpu_progressBar.setValue(0)
        self.model.clear()
        
        gpu_file_dict = gpuData.get_assets_gpuData()   
        if not gpu_file_dict:
            return 
            
        rowCount=0     
        for list in gpu_file_dict.keys():            
            nameItem = QtGui.QStandardItem(gpu_file_dict[list]['assetname'])
            chNameItem = QtGui.QStandardItem(gpu_file_dict[list]['assetCHName'])            
            insceneItem = QtGui.QStandardItem(gpu_file_dict[list]['inscene'])
            
            verDict = gpu_file_dict[list]['version']
            verDictItem = QtGui.QStandardItem(str(verDict))
            verItem = QtGui.QStandardItem(verDict.keys()[0])
            
            preivewPath = verDict.values()[0].replace('.yml','.jpg')
            if not os.path.isfile(preivewPath):
                preivewPath = ''
            previewItem = QtGui.QStandardItem(preivewPath)
            
            self.model.setItem(rowCount,0,previewItem)
            self.model.setItem(rowCount,1,chNameItem)
            self.model.setItem(rowCount,2,nameItem)
            self.model.setItem(rowCount,3,verItem)            
            self.model.setItem(rowCount,4,verDictItem)
            self.model.setItem(rowCount,5,insceneItem)
                        
            self.tableView.setItemDelegateForColumn(0,ReferenceImageDelegate(self.tableView))
            self.tableView.openPersistentEditor(self.proxy_model.index(rowCount,0))
            
            self.tableView.setItemDelegateForColumn(3,ComboDelegate(self.tableView))
            #self.tableView.openPersistentEditor(self.proxy_model.index(rowCount,3))
            
            #设置表格内文字居中
            self.model.item(rowCount,1).setTextAlignment(QtCore.Qt.AlignCenter)
            self.model.item(rowCount,2).setTextAlignment(QtCore.Qt.AlignCenter)
            self.model.item(rowCount,3).setTextAlignment(QtCore.Qt.AlignCenter)
            
            rowCount += 1
            
        #设置表格横向标题,表格美化
        headList = ['preivew',u'资产中文名','assetName','latestVer','verDict']
        self.model.setHorizontalHeaderLabels(headList)
         
        #表格100撑满tableView,第一行锁住表格放大，qt5的话.setResizeMode改成.setSectionResizeMode 
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setResizeMode(1,QtGui.QHeaderView.Stretch)
        self.tableView.horizontalHeader().setResizeMode(2,QtGui.QHeaderView.Stretch)
        #设置单元格禁止更改  
        #self.tableView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers) 
        #self.tableView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers | QtGui.QAbstractItemView.DoubleClicked)
        
        #设置整行选择
        self.tableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        
        #设置单元格宽度
        self.tableView.setColumnWidth(0,100)
        self.tableView.setColumnWidth(1,150)
        self.tableView.setColumnWidth(2,200)
        self.tableView.setColumnWidth(3,80)
        self.tableView.verticalHeader().setDefaultSectionSize(80)
        self.tableView.resizeColumnToContents(1)
        self.tableView.resizeColumnToContents(2)
        #隐藏列
        self.tableView.setColumnHidden(4,True)
        self.tableView.setColumnHidden(5,True)
        
    def getDesc(self):
        hasSelection = not self.tableView.selectionModel().selection().isEmpty()
        if hasSelection:
            get_select_index_list = self.tableView.selectionModel().selectedRows()
            for i,index in enumerate(get_select_index_list):  
                row = index.row()                
                get_select_dict = self.model.data(self.model.index(row,4))
                get_select_ver = self.model.data(self.model.index(row,3))
                verDict = eval(get_select_dict)        
                gpu_yamlFile = verDict[get_select_ver]
                getYaml = jarryLibs.dict2yaml(gpu_yamlFile).read()
                desc = getYaml['dec']
                #print get_select_ver
                #return desc
                
                self.declaration_tex.setText(desc)
    def load_gpu(self):
        hasSelection = not self.tableView.selectionModel().selection().isEmpty()
        if hasSelection:
            get_select_index_list = self.tableView.selectionModel().selectedRows()
            for i,index in enumerate(get_select_index_list):  
                row = index.row()                
                get_select_dict = self.model.data(self.model.index(row,4))
                get_select_ver = self.model.data(self.model.index(row,3))
                get_select_name = self.model.data(self.model.index(row,2))
                verDict = eval(get_select_dict)        
                gpu_yamlFile = verDict[get_select_ver]
                #print self.tableView.selectionModel().select()
                gpu2do = lg.load_gpuCache_dict(gpu_yamlFile)
                for x in gpu2do:
                    #x/len(get_select_index_list)
                    self.loadGpu_progressBar.setValue(x)
                self.loadGpu_progressBar.setValue(100)
            logging.info('finish!!')
    def load_single_gpu(self):
        hasSelection = not self.tableView.selectionModel().selection().isEmpty()
        if hasSelection:
            get_select_index_list = self.tableView.selectionModel().selectedRows()
            for x,index in enumerate(get_select_index_list):                
                row = index.row()                
                get_select_dict = self.model.data(self.model.index(row,4))
                get_select_ver = self.model.data(self.model.index(row,3))
                get_select_name = self.model.data(self.model.index(row,2))
                verDict = eval(get_select_dict)        
                gpu_yamlFile = verDict[get_select_ver]
                #print self.tableView.selectionModel().select()
                lg.load_gpuCache_single(gpu_yamlFile)
                self.loadGpu_progressBar.setValue(x)
            self.loadGpu_progressBar.setValue(100)
            logging.info('finish!!')

    def gpu2abc(self):
        import gpu2abc as g2a
        reload(g2a)
        g2a.gpu_conver_mesh()
        
        
def run(dock=False):
    name = 'envGpuToolUI'
    if pm.window(name, q=1, ex=1):
        pm.deleteUI(name)
    ui = gpu_mainUI(parent=getMayaWindow())
    
    if not dock:
        ui.show()
    else:
        dockName = 'envGpuTool'

        if pm.dockControl(dockName, q=1, ex=1):
            pm.deleteUI(dockName)


        pm.dockControl(dockName, area='right',
                     content = ui.objectName(),
                     width=370,
                     label=ui.objectName(),
                     allowedArea=['right', 'left'])
                     
                     
if __name__ == "__main__":    
    my_ui = gpu_mainUI()   
    
    my_ui.show()
    #app.exec_()    
    
        
        


