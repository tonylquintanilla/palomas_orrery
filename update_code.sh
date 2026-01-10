#!/bin/bash

# Change to the directory where this script is located
cd "$(dirname "$0")"

# Safety check - make sure we're in the right folder
if [ ! -f "palomas_orrery.py" ]; then
    echo ""
    echo "============================================"
    echo "ERROR: Wrong location!"
    echo "============================================"
    echo ""
    echo "This script must be inside your palomas_orrery folder."
    echo ""
    echo "Please move update_code.sh into the folder containing"
    echo "palomas_orrery.py and run it again."
    echo ""
    echo "Current location: $(pwd)"
    echo ""
    read -p "Press Enter to exit..."
    exit 1
fi

echo "============================================"
echo "Paloma's Orrery - Code Update Script"
echo "============================================"
echo ""
echo "This will update your Python code to the latest version."
echo "Your data files (orbit cache, star catalogs) will be preserved."
echo ""
echo "Location: $(pwd)"
echo ""
read -p "Press Enter to continue..."

# Check if already a git repo
if [ -d ".git" ]; then
    echo ""
    echo "Updating from GitHub..."
    git pull
else
    echo ""
    echo "First-time setup - connecting to GitHub..."
    git init
    git remote add origin https://github.com/tonylquintanilla/palomas_orrery.git
    git fetch origin
    git reset --hard origin/main
fi

echo ""
echo "============================================"
echo "Update complete!"
echo "============================================"
echo ""
read -p "Press Enter to exit..."
