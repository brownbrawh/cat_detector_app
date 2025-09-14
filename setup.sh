#!/bin/bash

# Cat Detector MVP Setup Script
echo "🐱 Setting up Cat Detector MVP..."

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

# Check if pip3 is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip3 first."
    exit 1
fi

# Install dependencies
echo "📦 Installing dependencies..."
pip3 install -r requirements.txt

# Make the script executable
chmod +x cat_detector.py

# Create cat_photos directory
mkdir -p cat_photos

echo "✅ Setup complete!"
echo ""
echo "🚀 To run the app:"
echo "   python3 cat_detector.py"
echo ""
echo "📸 Photos will be saved in the 'cat_photos' directory"
echo "🎮 Controls: 'q' to quit, 's' for manual photo"

