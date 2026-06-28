from core.geometry import Geometry

print("Distance")
print(
    Geometry.distance(
        (0, 0),
        (3, 4)
    )
)

print()

print("180 Degree")
print(
    Geometry.angle(
        (0, 0),
        (1, 0),
        (2, 0)
    )
)

print()

print("90 Degree")
print(
    Geometry.angle(
        (0, 0),
        (1, 0),
        (1, 1)
    )
)