import sys
import os
parent_dir = os.path.dirname(os.getcwd())
sys.path.append(parent_dir)
import pdb
import pyFlightscript as pyfs

pyfs.initialization.open_fsm('other.fsm')
pyfs.script.display_lines()
pyfs.script.write_to_file()

print('~~~ Test Complete ~~~')