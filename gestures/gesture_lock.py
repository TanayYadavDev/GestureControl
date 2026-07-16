"""Simple lock to avoid repeated gesture triggers every frame."""

from gestures.gesture import NO_HAND_GESTURE, UNKNOWN_GESTURE


class GestureLock:
    """Emit a gesture once, then suppress repeats for a cooldown window."""

    def __init__(self, cooldown_frames: int = 8):
        self.cooldown_frames = max(0, int(cooldown_frames))
        self._last_emitted = None
        self._cooldown_left = 0

    def update(self, gesture_name: str) -> str:
        if self._cooldown_left > 0:
            self._cooldown_left -= 1

        if gesture_name in (UNKNOWN_GESTURE, NO_HAND_GESTURE):
            self._last_emitted = None
            return gesture_name

        if gesture_name == self._last_emitted and self._cooldown_left > 0:
            return UNKNOWN_GESTURE

        self._last_emitted = gesture_name
        self._cooldown_left = self.cooldown_frames
        return gesture_name

    def reset(self) -> None:
        self._last_emitted = None
        self._cooldown_left = 0
