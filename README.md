# GestureControl

Control your computer with hand gestures, real-time computer vision, and a lightweight gesture-recognition pipeline.

## What it does

GestureControl tracks your hand through the camera, analyzes finger geometry, and turns recognized gestures into actions you can build on.

- Real-time hand detection and landmark tracking
- Gesture analysis using finger angles and states
- Gesture recognition with a modular gesture database
- Frame stability filtering to reduce jitter
- Optional trigger locking to avoid repeated actions
- Camera overlay that shows FPS and the active gesture

## Supported gestures

The current gesture set includes:

| Gesture | Finger Pattern |
| --- | --- |
| `OPEN_PALM` | `1 1 1 1 1` |
| `FIST` | `0 0 0 0 0` |
| `POINT` | `0 1 0 0 0` |
| `PEACE` | `0 1 1 0 0` |
| `THUMBS_UP` | `1 0 0 0 0` |
| `VICTORY` | `0 1 0 0 1` |

## Tech stack

- Python
- OpenCV
- MediaPipe
- NumPy
- PyAutoGUI
- Pycaw

## Project structure

```text
GestureControl/
├── controllers/        # Media, mouse, and volume action handlers
├── core/               # Camera, geometry, hand analysis, and utilities
├── gestures/           # Gesture definitions, recognition, filters, and locks
├── assets/             # Media assets for docs and future demos
├── main.py             # Main camera loop and overlay
└── requirements.txt    # Python dependencies
```

## How it works

1. The camera captures each frame.
2. MediaPipe landmarks are extracted from the hand.
3. Finger joint angles are computed in `core/hand_analyzer.py`.
4. The recognizer maps the finger-state pattern to a gesture.
5. The result is shown on the camera overlay and can be connected to actions.

## Installation

> Recommended for Windows because the current controller stack includes `pycaw`.

```bash
git clone https://github.com/TanayYadavDev/GestureControl.git
cd GestureControl
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Run the app

```bash
python main.py
```

Press `q` to exit the camera window.

## Notes

- Make sure your webcam is available and not used by another app.
- Good lighting improves landmark detection.
- Keep your hand clearly visible in frame for the best gesture classification.
- If you extend the gesture set, update `gestures/gesture_database.py`.

## Roadmap

- Virtual mouse controls
- Brightness controls
- Custom user-defined gestures
- Air drawing mode
- More robust thumb classification and gesture tuning

## License

Add your preferred license here before publishing the project publicly.
