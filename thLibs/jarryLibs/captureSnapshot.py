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
import re
# Third-party modules
try:
    import maya.OpenMayaUI as mui
    from PySide import QtCore, QtGui
    import shiboken
    import maya.cmds as cmds
except:
    pass
 
class captureSnapshot():
    def __init__(self):
        pass
    @property    
    def getFirstVisibleModelPanel(self):
        visPanels = cmds.getPanel(vis=1)        
        for currentPanel in visPanels:
            panelType = cmds.getPanel(to=currentPanel)
            if panelType == "modelPanel":
                return currentPanel
                 
    def getMayaWindow(self):
      # Get the maya main window as a QMainWindow instance
        model = self.getFirstVisibleModelPanel
        if model:
            view = mui.M3dView.active3dView()
            widget_ptr = view.widget()
            ptr = mui.MQtUtil.findLayout(model)
            return shiboken.wrapInstance(long(widget_ptr), QtGui.QMainWindow)
            
    def capture(self):
        self.shnapshot = QtGui.QPixmap.grabWindow(self.getMayaWindow().winId())
        return self.shnapshot
        
    def saveImage(self,imagePath):
        self.shnapshot.save(imagePath)
        
    def capturePlayblast(self,imagePath):
        cmds.playblast( frame=cmds.currentTime(q=True),
                f=imagePath, 
                fo=True, fmt="image", viewer=False,width=1000, height=800,
                c="jpg", quality=100,percent=100 )
                

            
if __name__ == "__main__":
    pass

