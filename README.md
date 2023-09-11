## pyFlightscript

A python API for generating native FlightStream scripts.
This is an open source project, but is sponsored in part by Research In Flight. Development is on-going.

## Installation

No dependencies required at this time.

`python setup.py install`

## Features

- Generates FlightStream scripts with a user-friendly Pythonic interface
- Modules broken into categories for ease of search.

## Example code

```
import pyFlightscript as pyfs

pyfs.fsinit.open_fsm('test.fsm')
pyfs.script_state.display_lines()
pyfs.script_state.write_to_file()
```

## To generate new docs

within \sphinx directory

### on Windows

simply run `generate_docs.bat`

### on other systems

remove \_build directory
run 'sphinx-apidoc -o . ../pyFlightscript/'
rename pyFlighscript.rst to index.rst
run 'make.bat html'
docs are in '.\_build\html\index.html'

## Contribution

Contributions are welcome!

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

Please post bugs to the 'issues' section. Feel free to create a branch and submit a pull request. An admin will be notified.

## License

GNU AFFERO GENERAL PUBLIC LICENSE
