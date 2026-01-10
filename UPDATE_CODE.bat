@echo off
REM Change to the directory where this batch file is located
cd /d "%~dp0"

REM Safety check - make sure we're in the right folder
if not exist "palomas_orrery.py" (
    echo.
    echo ============================================
    echo ERROR: Wrong location!
    echo ============================================
    echo.
    echo This script must be inside your palomas_orrery folder.
    echo.
    echo Please move UPDATE_CODE.bat into the folder containing
    echo palomas_orrery.py and run it again.
    echo.
    echo Current location: %cd%
    echo.
    pause
    exit /b 1
)

echo ============================================
echo Paloma's Orrery - Code Update Script
echo ============================================
echo.
echo This will update your Python code to the latest version.
echo Your data files (orbit cache, star catalogs) will be preserved.
echo.
echo Location: %cd%
echo.
pause

REM Check if already a git repo
if exist ".git" (
    echo.
    echo Updating from GitHub...
    git pull
) else (
    echo.
    echo First-time setup - connecting to GitHub...
    git init
    git remote add origin https://github.com/tonylquintanilla/palomas_orrery.git
    git fetch origin
    git reset --hard origin/main
)

echo.
echo ============================================
echo Update complete!
echo ============================================
echo.
pause
