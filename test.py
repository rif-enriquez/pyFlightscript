import sys
import pdb
import pyFlightscript as pyfs

pyfs.open_fsm('test.txt', 'other.fsm')
pyfs.stop_script('test.txt')
pdb.set_trace()
