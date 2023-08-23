import sys
import os
parent_dir = os.path.dirname(os.getcwd())
sys.path.append(parent_dir)
import pdb
import pyFlightscript as pyfs

pyfs.open_fsm('test.txt', 'other.fsm')
pyfs.stop_script('test.txt')
pdb.set_trace()
