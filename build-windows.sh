#!/bin/bash

set -e

echo "[NiTROBLAST BUILD] Building binary..."
uv run pyinstaller src/nitro_blast/nitroblast.py --name NiTROBLAST\
 --add-data ./put-python-interpreters-here/:./python-interpreters/
echo "[NiTROBLAST BUILD] Building binary... - OK"

echo "[NiTROBLAST BUILD] Copying run-on-windows.bat next to executable..."
cp ./src/nitro_blast/run-on-windows.bat ./dist/NiTROBLAST/
echo "[NiTROBLAST BUILD] Copying run-on-windows.bat next to executable... - OK"

echo "[NiTROBLAST BUILD] Copying src to dist..."
cp -r ./src ./dist/NiTROBLAST/src
echo "[NiTROBLAST BUILD] Copying src to dist... - OK"

echo "[NiTROBLAST BUILD] Done!"
