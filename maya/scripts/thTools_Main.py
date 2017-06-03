#!/usr/bin/env python
# -*- coding: utf-8 -*-

import maya.cmds as cmds
import maya.mel as mm

def menuBar():  
    mainwindow = mm.eval('$temp = $gMainWindow;')
    if cmds.menu('TH_ToolsMenu',exists=1) == 1:
        cmds.deleteUI('TH_ToolsMenu')
    menuBarLayout = cmds.menuBarLayout()
    toolMenu = cmds.menu('TH_ToolsMenu',l=u'【 TH_Tools 】',to=1,parent = 'MayaWindow')

    cmds.menuItem( label='apps',to=1,subMenu = 1)
    cmds.menuItem( label='runPwSE',ann = u'pw_multiScriptEditor',c = "import sys;path = 'Z:/Resource/Support/th_repos/apps/';sys.path.append(path);import pw_multiScriptEditor;pw_multiScriptEditor.showMaya(dock=0)" )
    cmds.setParent('..',menu=True)
    
    cmds.menuItem( label='Model',to=1,subMenu=1 )
    cmds.menuItem( label='NodeRenameAlphaTool',ann = u'节点智能命名工具',c = 'import nodeRename.nodeRename as nr;reload(nr);nr.nodeRename().UI()')
    cmds.menuItem( label='CBrename',ann = u'chenbing命名工具',c = 'pm.mel.CBrename()' )
    cmds.menuItem( label='imageRenameAlphaTool',ann = u'贴图智能命名工具',c = 'import imageRename.imageRename as ir;reload(ir);ir.UI()' )
    cmds.menuItem( label='FileTextureManager',ann = u'贴图管理器',c = 'pm.mel.FileTextureManager()' )
    cmds.menuItem( label='UVswiftMover',ann = u'uv偏移工具',c = 'pm.mel.UVswiftMover()' )
    cmds.menuItem( label='resetNormal',ann = u'重组法线',c = 'pm.mel.resetNormal()' )
    cmds.setParent('..',menu=True)
    
    cmds.menuItem( label='Rendering',to=1,subMenu = 1)
    cmds.menuItem( label='DF:abcCacheShaderTools',ann = u'镜头abc缓存管理工具' ,c='from rendering.pycFunc import *;import rendering.pycFunc.Main as mmain;reload(mmain);mmain.run()')
    cmds.menuItem( label='DF:abcCacheBachExport',ann = u'abc缓存批量输出工具' ,c='import pymel.core as pm;import cacheTool.abcCacheBachExport_Main as abcexp;reload(abcexp);abcexp.abcCacheBachExportUI();')
    cmds.menuItem( label='camFocusDistance2Nuke',ann = u'将Arnold的焦距变化输出到nuke的zdfocus' ,c='import rendering.camFocusDistance2Nuke as arfd ;reload(arfd);arfd.camFocusDistance2Nuke();')
    #cmds.menuItem( label='killUnloadRef',ann = u'删除unload参考文件' ,c='import libs.tools as tht;reload(tht);tht.killUnloadRef();')
    #cmds.menuItem( label='DF:exportFur_shave',ann = u'导出fur_shave(身上绒毛)' ,c= 'import rendering.exportFurShave_With_DF_Publish as efs;reload(efs);efs.exportFur_shave()',en=0)
    #cmds.menuItem( label='DF:assignShader',ann = u'赋材质工具',en=0 )
    cmds.menuItem( label='renderStatsWinSwitch',ann = u'物体渲染属性设置',c = 'pm.mel.renderStatsWinSwitch()' )
    cmds.menuItem( label='DF:refreshReferneceFile',ann = u'更新reference列表中的资产版本为最新',c = 'pm.mel.refreshReferneceFile()' )
    #cmds.setParent('..',menu=True)
    #cmds.menuItem( label='cfx',to=1,subMenu = 1)
    #cmds.menuItem( label='DF:yeti fur pipline',ann = 'yeti fur pipline',en=1,c='import pymel.core as pm;import cfx.df_yetiPipline.df_YetiPiplineMain as ypm;reload(ypm);ypm.yetiPipline().UI()' )
    #cmds.menuItem( label='DF:clothCollAbcCacheBatchExport',ann = '',en=1,c='import pymel.core as pm;import cacheTool.abcCacheBachExportWithClothColl_Main as abcCexp;reload(abcCexp);abcCexp.abcCacheBachExportClothColl().abcCacheBachExportClothCollUI()' )
    cmds.setParent('..',menu=True)
    
    cmds.menuItem( label='assets',to=1,subMenu = 1)
    cmds.menuItem( label='gpuCacheTool',ann = 'gpuCacheTool Manager',en=1,c='import envGpuTool.envGpuTool_main as gpu_main;reload(gpu_main);gpu_main.run()' )
    
    cmds.setParent('..',menu=True)
    
    cmds.menuItem( label='publish',to=1,subMenu = 1)
    cmds.menuItem( label='publish gpuCache',ann = 'publish gpuCache',en=1,c='import envGpuTool.envGpuPublishTool_main as gpu_Pub_main;reload(gpu_Pub_main);gpu_Pub_main.run()' )
    cmds.setParent('..',menu=True)
if __name__ == "__main__":
    pass
    
    
