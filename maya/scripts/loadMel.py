#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import os
import pymel.core as pm
import thtk_log
import logging

file = os.path.dirname(__file__)
log = thtk_log.thtk_log(level=logging.INFO)

log.info("tyhooTK_Maya melLoading...")
melList = glob.glob(file + '/mel/*.mel')

for mel in melList:
    
    pm.mel.source(mel.replace('\\','/'))
    log.info("melLoading...->%s"%mel)
log.info("tyhooTK_Maya melLoading...Done")

if __name__ == "__main__":
    pass

