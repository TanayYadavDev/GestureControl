"""Gesture definitions and database lookup helpers."""

from typing import Iterable, List, Optional, Sequence, Tuple

from gestures.gesture import Gesture


def _normalize_pattern(pattern: Sequence[int]) -> Tuple[int, int, int, int, int]:
    if len(pattern) != 5:
        raise ValueError("Gesture pattern must contain exactly 5 finger states.")
    return tuple(int(v) for v in pattern)  # type: ignore[return-value]


DEFAULT_GESTURES: List[Gesture] = [
    Gesture("OPEN_PALM", (1, 1, 1, 1, 1)),
    Gesture("FIST", (0, 0, 0, 0, 0)),
    Gesture("POINT", (0, 1, 0, 0, 0)),
    Gesture("PEACE", (0, 1, 1, 0, 0)),
    Gesture("THUMBS_UP", (1, 0, 0, 0, 0)),
    Gesture("VICTORY", (0, 1, 0, 0, 1)),
]


class GestureDatabase:
    """Stores gesture definitions and resolves a finger pattern to a gesture."""

    def __init__(self, gestures: Optional[Iterable[Gesture]] = None):
        self._gestures = list(gestures) if gestures is not None else list(DEFAULT_GESTURES)

    def match_pattern(self, pattern: Sequence[int]) -> Optional[Gesture]:
        normalized = _normalize_pattern(pattern)
        for gesture in self._gestures:
            if gesture.pattern == normalized:
                return gesture
        return None

    @property
    def gestures(self) -> List[Gesture]:
        return list(self._gestures)
