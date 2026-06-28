from core.hand_math import HandMath
from core.landmarks import *

THUMB_OPEN_ANGLE = 150
FINGER_OPEN_ANGLE = 160

class HandAnalyzer:

    def analyze(self, landmarks):

        if not landmarks:
            return None

        features = {}

        # -----------------------
        # Finger Angles
        # -----------------------

        features["angles"] = {

            "thumb":
                HandMath.finger_angle(
                    landmarks,
                    THUMB_MCP,
                    THUMB_IP,
                    THUMB_TIP
                ),

            "index":
                HandMath.finger_angle(
                    landmarks,
                    INDEX_MCP,
                    INDEX_PIP,
                    INDEX_TIP
                ),

            "middle":
                HandMath.finger_angle(
                    landmarks,
                    MIDDLE_MCP,
                    MIDDLE_PIP,
                    MIDDLE_TIP
                ),

            "ring":
                HandMath.finger_angle(
                    landmarks,
                    RING_MCP,
                    RING_PIP,
                    RING_TIP
                ),

            "pinky":
                HandMath.finger_angle(
                    landmarks,
                    PINKY_MCP,
                    PINKY_PIP,
                    PINKY_TIP
                ),
        }
        features["states"] = {

            finger: (
                angle > THUMB_OPEN_ANGLE
                if finger == "thumb"
                else angle > FINGER_OPEN_ANGLE
            )

            for finger, angle in features["angles"].items()
        }
        return features