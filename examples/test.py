import sys
import os
parent_dir = os.path.dirname(os.getcwd())
sys.path.append(parent_dir)
import pdb
import pyFlightscript as pyfs

pyfs.fsinit.open_fsm('other.fsm')
pyfs.script_state.display_lines()
pyfs.script_state.write_to_file()

print('~~~ Test Complete ~~~')