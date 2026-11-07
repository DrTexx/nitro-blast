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

echo "[NiTROBLAST BUILD] Creating directory for tools in ./dist..."
mkdir -p ./dist/tools
echo "[NiTROBLAST BUILD] Creating directory for tools in ./dist... - OK"

echo "[NiTROBLAST BUILD] Installing Prime95 into ./dist/tools ..."
install -m 755 ./put-programs-here/Prime95 ./dist/tools/Prime95
echo "[NiTROBLAST BUILD] Installing Prime95 into ./dist/tools ... - OK"

echo "[NiTROBLAST BUILD] Installing Furmark into ./dist/tools ..."
install -m 755 ./put-programs-here/Prime95 ./dist/tools/Prime95
echo "[NiTROBLAST BUILD] Installing Furmark into ./dist/tools ... - OK"

echo "[NiTROBLAST BUILD] Installing FFXV Windows Edition Benchmark into ./dist/tools ..."
install -m 755 ./put-programs-here/FFXV-WE-benchmark ./dist/tools/FFXV-WE-benchmark
echo "[NiTROBLAST BUILD] Installing FFXV Windows Edition Benchmark into ./dist/tools ... - OK"

echo "[NiTROBLAST BUILD] Done!"
