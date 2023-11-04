@echo off
echo locating source
cd source
echo compiling...
python -m PyInstaller --onefile sketch.py
echo moving to release folder
move Z:\Home\Softworks\sketch\source\dist\sketch.exe Z:\Home\Softworks\sketch\release\Windows
echo creating contents folder
mkdir Z:\Home\Softworks\sketch\release\Windows\Sketch-Library
echo copying contents
copy Z:\Home\Softworks\sketch\source\Sketch-Library Z:\Home\Softworks\sketch\release\Windows\Sketch-Library
echo deleting temporary files
del Z:\Home\Softworks\sketch\source\sketch.spec
rmdir /s Z:\Home\Softworks\sketch\source\build -y
rmdir /s Z:\Home\Softworks\sketch\source\dist -y
echo done
pause