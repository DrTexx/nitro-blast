#!/bin/bash

echo "Building binary..."
uv run pyinstaller src/nitro_blast/nitroblast.py --name NiTROBLAST\
 --add-data ./put-python-interpreters-here/:./python-interpreters/\
cp ./src/nitro_blast/run-on-windows.bat ./dist/NiTROBLAST/
echo "Done!"
