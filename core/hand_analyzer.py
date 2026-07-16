from core.hand_math import HandMath
from core.landmarks import *

THUMB_OPEN_ANGLE = 148
FINGER_OPEN_ANGLE = 160
THUMB_DOMINANT_MCP_ANGLE = 148
THUMB_SUPPORT_IP_ANGLE = 135

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

            "thumb_base":
                HandMath.finger_angle(
                    landmarks,
                    THUMB_CMC,
                    THUMB_MCP,
                    THUMB_IP
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

        thumb_tip_angle = features["angles"]["thumb"]
        thumb_base_angle = features["angles"]["thumb_base"]

        thumb_open = (
            thumb_base_angle > THUMB_DOMINANT_MCP_ANGLE
            or (
                thumb_base_angle > THUMB_SUPPORT_IP_ANGLE
                and thumb_tip_angle > THUMB_OPEN_ANGLE
            )
        )

        features["states"] = {
            "thumb": thumb_open,
            "index": features["angles"]["index"] > FINGER_OPEN_ANGLE,
            "middle": features["angles"]["middle"] > FINGER_OPEN_ANGLE,
            "ring": features["angles"]["ring"] > FINGER_OPEN_ANGLE,
            "pinky": features["angles"]["pinky"] > FINGER_OPEN_ANGLE,
        }
        return features