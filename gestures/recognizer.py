from typing import Iterable, Mapping, Optional, Sequence

from gestures.gesture import FINGER_ORDER, UNKNOWN_GESTURE
from gestures.gesture_database import GestureDatabase
from gestures.gesture_lock import GestureLock
from gestures.temporal_filter import TemporalFilter


class GestureRecognizer:

    def __init__(
        self,
        gesture_database: Optional[GestureDatabase] = None,
        stability_frames: int = 3,
        lock_cooldown_frames: int = 8,
        enable_temporal_filter: bool = True,
        enable_lock: bool = False,
    ):
        self.database = gesture_database or GestureDatabase()
        self.temporal_filter = (
            TemporalFilter(stability_frames=stability_frames)
            if enable_temporal_filter
            else None
        )
        self.gesture_lock = (
            GestureLock(cooldown_frames=lock_cooldown_frames)
            if enable_lock
            else None
        )

    def _to_finger_pattern(self, data) -> Optional[Sequence[int]]:
        if isinstance(data, Mapping):
            if "states" in data and isinstance(data["states"], Mapping):
                states = data["states"]
                return [1 if bool(states.get(finger, False)) else 0 for finger in FINGER_ORDER]

            if all(finger in data for finger in FINGER_ORDER):
                return [1 if bool(data[finger]) else 0 for finger in FINGER_ORDER]

            return None

        if isinstance(data, Iterable) and not isinstance(data, (str, bytes)):
            pattern = list(data)
            if len(pattern) == 5:
                return [1 if bool(value) else 0 for value in pattern]

        return None

    def recognize(self, data):
        pattern = self._to_finger_pattern(data)
        if pattern is None:
            return UNKNOWN_GESTURE

        matched = self.database.match_pattern(pattern)
        gesture_name = matched.name if matched else UNKNOWN_GESTURE

        if self.temporal_filter is not None:
            gesture_name = self.temporal_filter.update(gesture_name)

        if self.gesture_lock is not None:
            gesture_name = self.gesture_lock.update(gesture_name)

        return gesture_name