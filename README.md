# 🐱 Cat Detector MVP

A simple macOS app that automatically takes pictures when a cat is detected in the camera view.

## Features

- **Automatic Cat Detection**: Uses OpenCV's Haar cascade classifier to detect cats in real-time
- **Auto Photo Capture**: Automatically saves photos when cats are detected (with 5-second cooldown)
- **Manual Photo Capture**: Press 's' to take a manual photo anytime
- **Real-time Preview**: Live camera feed with detection boxes around detected cats
- **Photo Organization**: All photos are saved in a `cat_photos` directory with timestamps

## Requirements

- macOS (tested on macOS 14.5.0)
- Python 3.7+
- Camera access permission
- OpenCV and NumPy

## Installation

### Option 1: Clone from GitHub
1. **Clone this repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/cat_detector_app.git
   cd cat_detector_app
   ```

2. **Install Python dependencies**
   ```bash
   pip3 install -r requirements.txt
   ```

3. **Grant camera permissions** (if prompted by macOS)

### Option 2: Download ZIP
1. **Download and extract** the project files
2. **Navigate to the project directory**
   ```bash
   cd cat_detector_app
   ```
3. **Install dependencies and run** (same as above)

## Usage

1. **Run the app**
   ```bash
   python3 cat_detector.py
   ```

2. **Controls**
   - `q` - Quit the application
   - `s` - Take a manual photo
   - The app will automatically capture photos when cats are detected

3. **Photos are saved in** `cat_photos/` directory with filenames like:
   - `cat_auto_20241201_143022.jpg` (automatic detection)
   - `cat_manual_20241201_143045.jpg` (manual capture)

## How It Works

- Uses OpenCV's pre-trained Haar cascade classifier for cat face detection
- Processes video frames in real-time
- Draws green bounding boxes around detected cats
- Implements a 5-second cooldown between automatic captures to avoid spam
- Saves photos with timestamps for easy organization

## Troubleshooting

- **Camera not working**: Make sure no other app is using the camera
- **Permission denied**: Grant camera access in System Preferences > Security & Privacy
- **No cats detected**: The classifier works best with clear, well-lit images of cats facing the camera

## Future Enhancements

- Multiple cat detection
- Custom detection sensitivity settings
- Photo filtering and organization
- Cloud storage integration
- Mobile app version

Enjoy capturing your feline friends! 🐾

