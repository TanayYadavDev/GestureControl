import cv2
import mediapipe as mp


class HandDetector:

    def __init__(
        self,
        max_hands=1,
        detection_confidence=0.7,
        tracking_confidence=0.7
    ):

        self.mp_hands = mp.solutions.hands

        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=max_hands,
            min_detection_confidence=detection_confidence,
            min_tracking_confidence=tracking_confidence
        )

        self.drawer = mp.solutions.drawing_utils

    def detect(self, frame, draw=True):

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        self.results = self.hands.process(rgb)

        if self.results.multi_hand_landmarks:

            for hand in self.results.multi_hand_landmarks:

                if draw:
                    self.drawer.draw_landmarks(
                        frame,
                        hand,
                        self.mp_hands.HAND_CONNECTIONS
                    )

        return frame

    def get_landmarks(self, frame, hand_no=0, draw=True):

        landmark_list = []

        if self.results.multi_hand_landmarks:

            hand = self.results.multi_hand_landmarks[hand_no]

            h, w, _ = frame.shape

            for idx, lm in enumerate(hand.landmark):

                x = int(lm.x * w)
                y = int(lm.y * h)

                landmark_list.append((idx, x, y))

                if draw:
                    cv2.putText(
                        frame,
                        str(idx),
                        (x, y),
                        cv2.FONT_HERSHEY_PLAIN,
                        1,
                        (0, 255, 255),
                        1
                    )

        return landmark_list
