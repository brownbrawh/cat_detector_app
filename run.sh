#!/bin/bash

# Cat Detector MVP Launcher
echo "🐱 Starting Cat Detector MVP..."
echo "Make sure to grant camera permissions when prompted!"
echo ""

# Check if dependencies are installed
if ! python3 -c "import cv2, numpy" 2>/dev/null; then
    echo "❌ Dependencies not found. Running setup..."
    ./setup.sh
fi

# Run the cat detector
python3 cat_detector.py

