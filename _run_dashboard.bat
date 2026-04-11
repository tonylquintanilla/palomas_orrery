@echo off
REM ================================================================
REM  PALOMA'S ORRERY - DASHBOARD LAUNCHER
REM ================================================================
REM  Project: Paloma's Orrery - Astronomical Visualization System
REM  Author: Tony Quintanilla
REM  Contact: tonyquintanilla@gmail.com
REM  Version: 1.0
REM  
REM  Description:
REM    Launches the central Paloma's Orrery Dashboard.
REM    All visualization tools are accessible from the dashboard.
REM  
REM  Philosophy: "Data Preservation is Climate Action"
REM ================================================================

echo.
echo ============================================================
echo     PALOMA'S ORRERY - Dashboard
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

REM Check if dashboard exists
if not exist "%SCRIPT_DIR%palomas_orrery_dashboard.py" (
    echo ERROR: palomas_orrery_dashboard.py not found!
    echo.
    echo Please ensure this batch file is in the same
    echo directory as palomas_orrery_dashboard.py
    echo.
    echo Current directory: %SCRIPT_DIR%
    echo.
    pause
    exit /b 1
)

REM Check if customtkinter is installed
python -c "import customtkinter" >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing CustomTkinter...
    pip install customtkinter
    echo.
)

REM Change to the script directory
cd /d "%SCRIPT_DIR%"

echo Starting Dashboard...
echo Working directory: %cd%
echo.

REM Run the dashboard
python palomas_orrery_dashboard.py

REM Check exit code
if %errorlevel% neq 0 (
    echo.
    echo ============================================================
    echo     ERROR: Dashboard exited with code %errorlevel%
    echo ============================================================
    echo.
    echo Common issues:
    echo   - Missing packages: pip install customtkinter
    echo   - Python version: Requires Python 3.11+
    echo.
    pause
) else (
    echo.
    echo     Dashboard closed.
    echo.
    timeout /t 2
)
