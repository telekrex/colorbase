#!/bin/bash
echo "locating source"
cd source
echo "compiling..."
python3 -m PyInstaller --onefile sketch.py
echo "moving to release folder"
mv ./dist/sketch /home/azrael/private-server/Home/Softworks/sketch/release/Linux
echo "done"
echo "you will have to manually copy the Sketch-Library folder."