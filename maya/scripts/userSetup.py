# coding=utf8
# Copyright (c) 2016 

import sys
import os
import glob
import logging
import pymel.core as pm
import maya.mel as mel
import thtk_log



log = thtk_log.thtk_log(level=logging.INFO)
log.info("tyhooTK_Maya initializing...")


PROJECT_ROOT_NAME = "tyhooToolKit"
MODULE_PATH = pm.getModulePath(moduleName=PROJECT_ROOT_NAME)
# find the root dir path
# todo: I hate this shit
root_path = os.path.join(MODULE_PATH.split(PROJECT_ROOT_NAME)[0], PROJECT_ROOT_NAME)
# add pyLibs path to env
pyLibs_path = os.path.join(root_path, "pyLibs")
egg_list = glob.glob(r"%s\*.egg" % pyLibs_path)
for egg_path in egg_list:
    log.debug("Add %s into PYTHONPATH." % egg_path)
    sys.path.append(egg_path)
log.info("tyhooTK_Maya initialized...")

import loadMel
# add mel file
import maya.utils as mu
mu.executeDeferred("import thTools_Main;reload(thTools_Main);thTools_Main.menuBar()")
#add menu
#import thTools_Main;reload(thTools_Main);thTools_Main.menuBar()
log.info("Add all modules from pyLibs to PYTHONPATH Done.")
