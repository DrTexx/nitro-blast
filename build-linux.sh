#!/bin/bash

echo "Building binary..."
uv run pyinstaller src/nitro_blast/nitroblast.py --name NiTROBLAST --onefile
mkdir -p ./dist/tools/
install -m 755 ./put-programs-here/FIRESTARTER/FIRESTARTER ./dist/tools/FIRESTARTER
echo "Done!"
