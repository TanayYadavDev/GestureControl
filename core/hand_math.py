from core.geometry import Geometry


class HandMath:

    @staticmethod
    def point(landmarks, idx):
        """
        Returns (x, y) coordinates of a landmark.
        """

        _, x, y = landmarks[idx]

        return (x, y)

    @staticmethod
    def finger_angle(landmarks, mcp, pip, tip):
        """
        Returns bending angle of a finger.
        """

        return Geometry.angle(
            HandMath.point(landmarks, mcp),
            HandMath.point(landmarks, pip),
            HandMath.point(landmarks, tip)
        )

    @staticmethod
    def distance(landmarks, p1, p2):
        """
        Distance between two landmarks.
        """

        return Geometry.distance(
            HandMath.point(landmarks, p1),
            HandMath.point(landmarks, p2)
        )

    @staticmethod
    def midpoint(landmarks, p1, p2):
        """
        Midpoint of two landmarks.
        """

        return Geometry.midpoint(
            HandMath.point(landmarks, p1),
            HandMath.point(landmarks, p2)
        )