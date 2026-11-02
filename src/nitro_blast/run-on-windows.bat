@echo off
echo Launching...
cd _internal\python-interpreters\python314_64bit
@REM start "" "python.exe" -i -c "print('Hello, World!')"
start "" "python.exe" ../../../../../script-test.py
