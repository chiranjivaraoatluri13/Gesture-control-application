# Gesture Control for Media Playback

This Python project uses **MediaPipe** and **OpenCV** to recognize hand gestures via webcam and control media playback. It currently supports YouTube and can be extended for other platforms.

## Features
- **Play/Pause** with an open palm.
- **Rewind** with 1 finger (index).
- **Forward** with 2 fingers (index + middle).
- Optimized gesture detection with debounce to avoid accidental commands.

## Requirements
- Python 3.x
- OpenCV (`opencv-python`)
- MediaPipe (`mediapipe`)

## Installation
```sh
pip install opencv-python mediapipe
