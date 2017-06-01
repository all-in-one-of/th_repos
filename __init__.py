import os
import sys

# add parent path to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, current_dir)
sys.path.insert(0, parent_dir)
sys.path.insert(0, os.path.join(current_dir,'cgtkLibs'))
sys.path.insert(0, os.path.join(current_dir,'pyLibs'))
sys.path.insert(0, os.path.join(current_dir,'thLibs'))
