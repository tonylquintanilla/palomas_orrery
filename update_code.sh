#!/bin/bash
echo "============================================"
echo "Paloma's Orrery - Code Update Script"
echo "============================================"
echo ""
echo "This will update your Python code to the latest version."
echo "Your data files (orbit cache, star catalogs) will be preserved."
echo ""
read -p "Press Enter to continue..."

cd "$(dirname "$0")"

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
