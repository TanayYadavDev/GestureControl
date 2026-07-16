import cv2
import time

from core.camera import Camera
from core.hand_detector import HandDetector
from core.hand_analyzer import HandAnalyzer
from gestures.recognizer import GestureRecognizer
from gestures.gesture import NO_HAND_GESTURE

camera = Camera()
detector = HandDetector()
analyzer = HandAnalyzer()
recognizer = GestureRecognizer()
supported_gestures = [gesture.name for gesture in recognizer.database.gestures]

prev_time = time.time()

while True:

    frame = camera.read()

    if frame is None:
        break

    # -------------------------
    # Detect Hand
    # -------------------------

    detector.detect(frame)

    landmarks = detector.get_landmarks(frame)

    if landmarks:

        # -------------------------
        # Geometry Analysis
        # -------------------------

        features = analyzer.analyze(landmarks)

        # Temporary
        print(
            features["angles"],
            features["states"]
        )

        # Gesture Recognition
        if features:
            gesture = recognizer.recognize(features)

    else:
        gesture = NO_HAND_GESTURE

    # -------------------------
    # FPS
    # -------------------------

    current_time = time.time()

    fps = 1 / (current_time - prev_time)
    prev_time = current_time

    cv2.putText(
        frame,
        f"FPS : {int(fps)}",
        (20, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    cv2.putText(
        frame,
        f"Gesture: {gesture}",
        (20, 75),
        cv2.FONT_HERSHEY_SIMPLEX,   
        0.9,
        (255, 255, 0),
        2
    )

    cv2.putText(
        frame,
        "Supported: " + " | ".join(supported_gestures),
        (20, 110),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.55,
        (255, 255, 255),
        1
    )

    cv2.imshow("Gesture Control", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()