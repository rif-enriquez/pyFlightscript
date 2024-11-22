import sys, os
import pyFlightscript as pyfs
import pdb

# FLIGHTSTREAM EXE FILE PATH
fsexe_path = r'C:\Program Files\FlightStream\FlightStream.exe'

# GENERATE MACRO COMMANDS
pyfs.open_fsm(r'.\test.fsm')
pyfs.display_lines()
pyfs.close_flightstream()
pyfs.write_to_file() # write out the script txt file that will be run

## ALL COMMANDS GENERATED, NOW EXECUTE
pyfs.run_script(fsexe_path=fsexe_path) # run the macro in fs
pyfs.hard_reset() # delete script file and clear memory

print('~~~ Test Complete ~~~')