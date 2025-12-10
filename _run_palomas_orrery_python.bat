@echo off
REM ================================================================
REM  PALOMA'S ORRERY - PYTHON LAUNCHER
REM ================================================================
REM  Project: Paloma's Orrery - Astronomical Visualization System
REM  Author: Tony Quintanilla
REM  Contact: tonyquintanilla@gmail.com
REM  Version: 1.0
REM  
REM  Description:
REM    Launches the main Paloma's Orrery GUI from Python source.
REM    Use this for development or if you have Python installed.
REM  
REM  Philosophy: "Data Preservation is Climate Action"
REM ================================================================

echo.
echo ============================================================
echo     PALOMA'S ORRERY - Solar System Visualization
echo ============================================================
echo     Author: Tony Quintanilla
echo     "Data Preservation is Climate Action"
echo ============================================================
echo.

REM Store the directory where this batch file is located
set SCRIPT_DIR=%~dp0

REM Check if Python is installed and accessible
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo.
    echo Please install Python 3.11 or later from:
    echo https://www.python.org/downloads/
    echo.
    echo Ensure "Add Python to PATH" is checked during installation.
    echo.
    pause
    exit /b 1
)

REM Display Python version
echo Python detected:
python --version
echo.

REM Check if palomas_orrery.py exists
if not exist "%SCRIPT_DIR%palomas_orrery.py" (
    echo ERROR: palomas_orrery.py not found!
    echo.
    echo Please ensure this batch file is in the same 
    echo directory as palomas_orrery.py
    echo.
    echo Current directory: %SCRIPT_DIR%
    echo.
    pause
    exit /b 1
)

REM Change to the script directory
cd /d "%SCRIPT_DIR%"

echo Starting Paloma's Orrery...
echo Working directory: %cd%
echo.
echo ============================================================
echo.

REM Run the Python script
python palomas_orrery.py

REM Check exit code
if %errorlevel% neq 0 (
    echo.
    echo ============================================================
    echo     ERROR: Script exited with code %errorlevel%
    echo ============================================================
    echo.
    echo Common issues:
    echo   - Missing packages: pip install -r requirements.txt
    echo   - Python version: Requires Python 3.11+
    echo   - File permissions or antivirus blocking
    echo.
    pause
) else (
    echo.
    echo ============================================================
    echo     Paloma's Orrery closed successfully
    echo ============================================================
    echo.
    timeout /t 3
)
