import sys
import pdb
import pyFlightscript as pyfs

# print(dir(pyfs))
pyfs.open_fsm('test.txt', 'other.fsm')
pyfs.stop_script('test.txt')
pdb.set_trace()
