@echo off

REM Check for Python
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Please install Python 3.7 or newer from https://www.python.org/downloads/ and rerun this script.
    pause
    exit /b 1
)

REM Set up virtual environment
IF NOT EXIST venv (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Upgrade pip
python -m pip install --upgrade pip

REM Install dependencies
pip install -r requirements.txt

REM Run the app
python app.py

REM Keep window open if app exits
pause 