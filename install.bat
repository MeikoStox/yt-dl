@setlocal enableextensions
@cd /d "%~dp0"
@echo off
python -m pip install -r requirements.txt
cls
python ./setup.py
pause