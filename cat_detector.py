#!/usr/bin/env python3
"""
Cat Detection MVP App
Automatically takes pictures when a cat is detected in the camera view.
"""

import cv2
import numpy as np
import os
from datetime import datetime
import time

class CatDetector:
    def __init__(self):
        # Initialize the camera
        self.camera = cv2.VideoCapture(0)
        if not self.camera.isOpened():
            raise Exception("Could not open camera")
        
        # Load the cat detection cascade classifier
        self.cat_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalcatface.xml')
        
        # Create output directory for cat photos
        self.output_dir = "cat_photos"
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Detection parameters
        self.detection_threshold = 0.3
        self.last_detection_time = 0
        self.cooldown_period = 5  # seconds between detections
        
        print("🐱 Cat Detector MVP Started!")
        print("Press 'q' to quit, 's' to take manual photo")
        print("Camera will automatically capture photos when cats are detected!")

    def detect_cats(self, frame):
        """Detect cats in the frame using Haar cascade classifier"""
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cats = self.cat_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )
        return cats

    def save_photo(self, frame, reason="auto"):
        """Save the current frame as a photo"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.output_dir}/cat_{reason}_{timestamp}.jpg"
        cv2.imwrite(filename, frame)
        print(f"📸 Photo saved: {filename}")
        return filename

    def draw_detection_boxes(self, frame, cats):
        """Draw bounding boxes around detected cats"""
        for (x, y, w, h) in cats:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, 'Cat Detected!', (x, y-10), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        return frame

    def run(self):
        """Main detection loop"""
        try:
            while True:
                ret, frame = self.camera.read()
                if not ret:
                    print("Failed to read from camera")
                    break
                
                # Flip frame horizontally for mirror effect
                frame = cv2.flip(frame, 1)
                
                # Detect cats
                cats = self.detect_cats(frame)
                
                # Draw detection boxes
                if len(cats) > 0:
                    frame = self.draw_detection_boxes(frame, cats)
                    
                    # Auto-capture photo if cooldown period has passed
                    current_time = time.time()
                    if current_time - self.last_detection_time > self.cooldown_period:
                        self.save_photo(frame, "auto")
                        self.last_detection_time = current_time
                
                # Add status text
                status_text = f"Cats detected: {len(cats)}"
                cv2.putText(frame, status_text, (10, 30), 
                           cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                
                # Display the frame
                cv2.imshow('Cat Detector MVP', frame)
                
                # Handle key presses
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                    break
                elif key == ord('s'):
                    self.save_photo(frame, "manual")
                
        except KeyboardInterrupt:
            print("\nShutting down...")
        finally:
            self.cleanup()

    def cleanup(self):
        """Clean up resources"""
        self.camera.release()
        cv2.destroyAllWindows()
        print("✅ Cat Detector stopped successfully!")

def main():
    try:
        detector = CatDetector()
        detector.run()
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Make sure your camera is connected and not being used by another app.")

if __name__ == "__main__":
    main()

