#!/usr/bin/env python3
"""
Simple camera test to verify the setup works
"""

import cv2
import sys

def test_camera():
    print("🔍 Testing camera access...")
    
    # Try to open camera
    camera = cv2.VideoCapture(0)
    
    if not camera.isOpened():
        print("❌ Could not open camera")
        print("Make sure:")
        print("1. Camera is connected")
        print("2. No other app is using the camera")
        print("3. Camera permissions are granted")
        return False
    
    print("✅ Camera opened successfully")
    
    # Try to read a frame
    ret, frame = camera.read()
    if not ret:
        print("❌ Could not read from camera")
        camera.release()
        return False
    
    print("✅ Camera is working properly")
    print(f"📐 Frame size: {frame.shape[1]}x{frame.shape[0]}")
    
    # Test OpenCV installation
    try:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        print("✅ OpenCV image processing works")
    except Exception as e:
        print(f"❌ OpenCV error: {e}")
        camera.release()
        return False
    
    # Test cat cascade classifier
    try:
        cat_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalcatface.xml')
        if cat_cascade.empty():
            print("❌ Cat cascade classifier not found")
            camera.release()
            return False
        print("✅ Cat detection classifier loaded")
    except Exception as e:
        print(f"❌ Cat classifier error: {e}")
        camera.release()
        return False
    
    camera.release()
    print("🎉 All tests passed! Ready to detect cats!")
    return True

if __name__ == "__main__":
    success = test_camera()
    sys.exit(0 if success else 1)

