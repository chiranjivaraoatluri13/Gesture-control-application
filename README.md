# Gesture Control for Media Playback

Control Android media playback with hand gestures captured from your webcam. Uses **MediaPipe** for hand tracking and **ADB** to send media key events to a connected phone or tablet.

## Features

- **Play/Pause**: open palm (4 extended fingers)
- **Rewind**: 1 finger (index)
- **Fast forward**: 2 fingers (index + middle)
- Debounced gesture detection to avoid accidental triggers
- Live webcam preview with landmark overlay

## Requirements

- Python 3.8+
- Webcam
- Android device with [USB debugging](https://developer.android.com/studio/debug/dev-options) enabled
- [ADB](https://developer.android.com/tools/adb) installed and on your PATH

## Installation

```bash
git clone https://github.com/chiranjivaraoatluri13/Gesture-control-application.git
cd Gesture-control-application
pip install -r requirements.txt
```

## Setup

1. Connect your Android device via USB (or wireless ADB).
2. Verify the connection:

```bash
adb devices
```

3. Open a media app (YouTube, Spotify, etc.) on the device.

## Usage

```bash
python python_gesture_control.py
```

| Gesture | Action |
|---------|--------|
| Open palm (4 fingers) | Play / Pause |
| 1 finger | Rewind |
| 2 fingers | Fast forward |

Press **ESC** to quit.

### Test hand tracking only

```bash
python hand_tracking_test.py
```

## Project structure

```
Gesture-control-application/
├── python_gesture_control.py   # Main gesture → ADB control loop
├── hand_tracking_test.py       # Webcam hand tracking demo
└── requirements.txt
```

## How it works

MediaPipe detects 21 hand landmarks per frame. The script counts extended fingers (index through pinky) and maps finger counts to `adb shell input keyevent` commands for media control. A 1.2 second debounce window prevents rapid duplicate commands.

## License

MIT
