@echo off
echo Launching...
cd _internal\python-interpreters\python314_64bit
@REM start "" "python.exe" -i -c "print('Hello, World!')"
@REM start "" "python.exe" ../../../../../script-test.py
start "" "python.exe" %~dp0/src/nitro_blast/nitroblast.py
