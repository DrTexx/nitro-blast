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

echo "[NiTROBLAST BUILD] Ensuring Tkinter is installed in portable Python environment..."
TKINTER_SOURCE_PY_DIR="${USERPROFILE}/AppData/Roaming/uv/python/cpython-3.14-windows-x86_64-none"
PATH_IN_DIST_TO_EMBEDDABLE_PY_DIR="dist/NiTROBLAST/_internal/python-interpreters/python314_64bit"
mkdir -p "${PATH_IN_DIST_TO_EMBEDDABLE_PY_DIR}/Lib"
mkdir -p "${PATH_IN_DIST_TO_EMBEDDABLE_PY_DIR}/DLLs"
cp -r "${TKINTER_SOURCE_PY_DIR}/tcl" "$(pwd)/${PATH_IN_DIST_TO_EMBEDDABLE_PY_DIR}/tcl"
cp -r "${TKINTER_SOURCE_PY_DIR}/Lib/tkinter" "$(pwd)/${PATH_IN_DIST_TO_EMBEDDABLE_PY_DIR}/Lib/tkinter"
install -t "$(pwd)/${PATH_IN_DIST_TO_EMBEDDABLE_PY_DIR}/DLLs/"\
 "${TKINTER_SOURCE_PY_DIR}/DLLs/_tkinter.pyd"\
 "${TKINTER_SOURCE_PY_DIR}/DLLs/tcl86t.dll"\
 "${TKINTER_SOURCE_PY_DIR}/DLLs/tk86t.dll"\
 "${TKINTER_SOURCE_PY_DIR}/DLLs/zlib1.dll"
echo "[NiTROBLAST BUILD] Ensuring Tkinter is installed in portable Python environment... - OK"

echo "[NiTROBLAST BUILD] Installing Prime95 into ./dist/tools ..."
install -dm 755 ./put-programs-here/Prime95/** ./dist/tools/Prime95
echo "[NiTROBLAST BUILD] Installing Prime95 into ./dist/tools ... - OK"

echo "[NiTROBLAST BUILD] Installing Furmark into ./dist/tools ..."
install -dm 755 ./put-programs-here/Furmark/** ./dist/tools/Furmark
echo "[NiTROBLAST BUILD] Installing Furmark into ./dist/tools ... - OK"

echo "[NiTROBLAST BUILD] Installing FFXV Windows Edition Benchmark into ./dist/tools ..."
install -dm 755 ./put-programs-here/FFXV-WE-benchmark/** ./dist/tools/FFXV-WE-benchmark
echo "[NiTROBLAST BUILD] Installing FFXV Windows Edition Benchmark into ./dist/tools ... - OK"

echo "[NiTROBLAST BUILD] Done!"
