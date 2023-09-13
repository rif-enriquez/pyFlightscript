import sys, os
import pyFlightscript as pyfs
import pdb

# FLIGHTSTREAM EXE FILE PATH
fsexe_path = r'C:\Users\Danie\AppData\Roaming\Research in Flight\FlightStream\FlightStream.exe'

# GENERATE MACRO COMMANDS
pyfs.fsinit.open_fsm(r'.\test.fsm')
pyfs.script.display_lines()
pyfs.exec_solver.close_flightstream()
pyfs.script.write_to_file() # write out the script txt file that will be run

## ALL COMMANDS GENERATED, NOW EXECUTE
pyfs.script.run_script(fsexe_path=fsexe_path) # run the macro in fs
pyfs.script.hard_reset() # delete script file and clear memory

print('~~~ Test Complete ~~~')