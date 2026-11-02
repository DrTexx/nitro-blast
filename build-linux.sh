#!/bin/bash

set -e

echo "[NiTROBLAST BUILD] Building binary..."
uv run pyinstaller src/nitro_blast/nitroblast.py --name NiTROBLAST --onefile
echo "[NiTROBLAST BUILD] Building binary... - OK"
echo "[NiTROBLAST BUILD] Installing FIRESTARTER into ./dist/tools ..."
mkdir -p ./dist/tools/FIRESTARTER
install -m 755 ./put-programs-here/FIRESTARTER/FIRESTARTER ./dist/tools/FIRESTARTER/FIRESTARTER
echo "[NiTROBLAST BUILD] Installing FIRESTARTER into ./dist/tools ... - OK"
echo "[NiTROBLAST BUILD] Done!"
