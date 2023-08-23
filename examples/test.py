import sys
import os

# Get the parent directory of the current working directory
parent_dir = os.path.dirname(os.getcwd())
# Append this path to sys.path
sys.path.append(parent_dir)

import pdb
import pyFlightscript as pyfs

# print(dir(pyfs))
pyfs.open_fsm('test.txt', 'other.fsm')
pyfs.stop_script('test.txt')
pdb.set_trace()
