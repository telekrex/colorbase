@echo off
echo locating source
cd source
echo compiling...
python -m PyInstaller --onefile colorbase.py -noconsole
echo moving to release folder
move  %~dp0\source\dist\colorbase.exe  %~dp0\release\Windows
echo done
pause