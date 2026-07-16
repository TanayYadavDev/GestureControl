"""Frame-based temporal stabilization for gesture labels."""

from gestures.gesture import UNKNOWN_GESTURE


class TemporalFilter:
    """Returns a gesture only after it appears for N consecutive frames."""

    def __init__(self, stability_frames: int = 3):
        self.stability_frames = max(1, int(stability_frames))
        self._candidate = UNKNOWN_GESTURE
        self._count = 0
        self._stable = UNKNOWN_GESTURE

    def update(self, gesture_name: str) -> str:
        if gesture_name == self._candidate:
            self._count += 1
        else:
            self._candidate = gesture_name
            self._count = 1

        if self._count >= self.stability_frames:
            self._stable = self._candidate

        return self._stable

    def reset(self) -> None:
        self._candidate = UNKNOWN_GESTURE
        self._count = 0
        self._stable = UNKNOWN_GESTURE
