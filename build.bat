@echo off
python -m pip install --upgrade pip
pip install -r requirements.txt
pyinstaller --onefile --noconsole --icon=fox.ico matrixCalc.py