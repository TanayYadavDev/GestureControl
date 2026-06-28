"""General utility helpers."""


def clamp(value, low, high):
    """Clamp value between low and high."""
    return max(low, min(value, high))
