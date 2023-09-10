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

## To generate new docs

within \docs directory
remove \_build directory
run 'sphinx-apidoc -o . ../pyFlightscript/'
rename pyFlighscript.rst to index.rst
run 'make.bat html'

## To Contribute

Fork the repository
Locally clone and set upstream project
Create a new branch
make changes and commit
Push changes to your fork
Open a Pull Request - Ensure the base repository is the original project and the head repository is your fork
Once your PR is approved, the maintainers will merge it.
