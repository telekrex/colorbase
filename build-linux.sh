#!/bin/bash
echo "locating source"
cd source
echo "compiling..."
python3 -m PyInstaller --onefile c.py
echo "done"