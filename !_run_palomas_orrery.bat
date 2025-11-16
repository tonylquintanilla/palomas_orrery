@echo off
REM ================================================================
REM  PALOMA'S ORRERY LAUNCHER
REM ================================================================
REM  Project: Paloma's Orrery - Astronomical Visualization System
REM  Author: Tony Quintanilla
REM  Contact: [tonyquintanilla@gmail.com]
REM  Version: 1.0
REM  Created: November 14, 2025
REM  Updated: November 14, 2025
REM  
REM  Description:
REM    Launches the Paloma's Orrery astronomical visualization
REM    system with comprehensive error checking and status display.
REM    Named after Paloma - transforming NASA/ESA data into
REM    interactive 3D visualizations of our cosmic neighborhood.
REM  
REM  Philosophy: "Data Preservation is Climate Action"
REM  
REM  Note: Windows shows a security warning for unsigned batch files.
REM        To avoid future warnings, uncheck "Always ask" when running.
REM ================================================================

echo.
echo ========================================
echo     PALOMA'S ORRERY - Starting Up
echo  Project: Paloma's Orrery - Astronomical Visualization System
echo  Author: Tony Quintanilla
echo  Contact: [tonyquintanilla@gmail.com]
echo ========================================
echo.

REM Store the directory where this batch file is located
set SCRIPT_DIR=%~dp0

REM Check if Python is installed and accessible
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python and ensure it's added to your system PATH
    echo.
    pause
    exit /b 1
)

REM Display Python version
echo Python detected:
python --version
echo.

REM Check if palomas_orrery.py exists in the current directory
if not exist "%SCRIPT_DIR%palomas_orrery.py" (
    echo ERROR: palomas_orrery.py not found in %SCRIPT_DIR%
    echo Please ensure this batch file is in the same directory as palomas_orrery.py
    echo.
    pause
    exit /b 1
)

REM Change to the script directory (in case launched from elsewhere)
cd /d "%SCRIPT_DIR%"

echo Starting Paloma's Orrery...
echo Working directory: %cd%
echo ----------------------------------------
echo.

REM Run the Python script
REM Using python instead of pythonw to see console output
python palomas_orrery.py

REM Check if the script ran successfully
if %errorlevel% neq 0 (
    echo.
    echo ========================================
    echo     ERROR: Script exited with error code %errorlevel%
    echo ========================================
    echo.
    echo Common issues to check:
    echo - Missing Python packages (numpy, pandas, plotly, etc.)
    echo - File permissions
    echo - Syntax errors in the script
    echo.
    echo To install required packages, run:
    echo pip install -r requirements.txt
    echo.
    pause
) else (
    echo.
    echo ========================================
    echo     Paloma's Orrery closed successfully
    echo ========================================
    echo.
    REM Optional: Comment out the next line if you want the window to close automatically on success
    timeout /t 3
)
