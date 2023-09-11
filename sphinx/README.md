## To generate new docs

within \sphinx directory

# on Windows

simply run generate_docs.bat

# on other

remove \_build directory
run 'sphinx-apidoc -o . ../pyFlightscript/'
rename pyFlighscript.rst to index.rst
run 'make.bat html'
docs are in '.\_build\html\index.html'
