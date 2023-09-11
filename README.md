### pyFlightscript

A python API for generating native FlightStream scripts.

#### Installation

No dependencies required at this time.

`python setup.py install`

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

## To generate new docs

within \sphinx directory

# on Windows

simply run `generate_docs.bat`

# on other

remove \_build directory
run 'sphinx-apidoc -o . ../pyFlightscript/'
rename pyFlighscript.rst to index.rst
run 'make.bat html'
docs are in '.\_build\html\index.html'
