### pyFlightscript

A python API for generating native FlightStream scripts.

#### Installation

No dependencies required at this time.

#### Features

- Generates FlightStream scripts with a user-friendly Pythonic interface
- Modules broken into categories for ease of search.

# Example code

```
import pyFlightscript as pyfs

pyfs.fsinit.open_fsm('test.fsm')
pyfs.script_state.display_lines()
pyfs.script_state.write_to_file()
```
