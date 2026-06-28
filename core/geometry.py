import math


class Geometry:
    """
    Pure geometry helper functions.

    Works only on (x, y) tuples.
    No OpenCV.
    No MediaPipe.
    """

    @staticmethod
    def distance(p1, p2):
        """
        Euclidean distance between two points.

        p1 = (x, y)
        p2 = (x, y)
        """

        return math.hypot(
            p2[0] - p1[0],
            p2[1] - p1[1]
        )
    
    @staticmethod
    def distance_sq(p1, p2):

        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]

        return dx*dx + dy*dy

    @staticmethod
    def vector(p1, p2):
        """
        Vector from p1 -> p2
        """

        return (
            p2[0] - p1[0],
            p2[1] - p1[1]
        )
    
    @staticmethod
    def cross(v1, v2):
        return (
            v1[0] * v2[1]
            -
            v1[1] * v2[0]
        )

    @staticmethod
    def magnitude(v):
        """
        Length of vector.
        """

        return math.hypot(v[0], v[1])

    @staticmethod
    def normalize(v):
        """
        Unit vector.
        """

        mag = Geometry.magnitude(v)

        if mag == 0:
            return (0.0, 0.0)

        return (
            v[0] / mag,
            v[1] / mag
        )

    @staticmethod
    def dot(v1, v2):
        """
        Dot product.
        """

        return (
            v1[0] * v2[0]
            +
            v1[1] * v2[1]
        )

    @staticmethod
    def angle(a, b, c):
        """
        Returns angle ABC in degrees.

             A

              •

               \

                \

                 •

                /

               /

              •

             C
        """

        ba = Geometry.vector(b, a)
        bc = Geometry.vector(b, c)

        mag_ba = Geometry.magnitude(ba)
        mag_bc = Geometry.magnitude(bc)

        if mag_ba == 0 or mag_bc == 0:
            return 0

        cos_theta = Geometry.dot(ba, bc) / (mag_ba * mag_bc)

        cos_theta = max(-1.0, min(1.0, cos_theta))

        return math.degrees(math.acos(cos_theta))

    @staticmethod
    def midpoint(p1, p2):
        """
        Midpoint of two points.
        """

        return (
            (p1[0] + p2[0]) / 2,
            (p1[1] + p2[1]) / 2
        )