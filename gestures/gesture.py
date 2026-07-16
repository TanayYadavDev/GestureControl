"""Gesture model and shared constants."""

from dataclasses import dataclass
from typing import Tuple

FINGER_ORDER = ("thumb", "index", "middle", "ring", "pinky")

UNKNOWN_GESTURE = "UNKNOWN"
NO_HAND_GESTURE = "NO HAND"


@dataclass(frozen=True)
class Gesture:
    """Represents a single gesture definition."""

    name: str
    pattern: Tuple[int, int, int, int, int]
