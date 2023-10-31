import math


# Good illustration of Class inheritance
# An Ellipsoid can be considered a general version of a sphere
class Ellipsoid:

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    def calculate_volume(self):
        volume = (4 * math.pi * self._a * self._b * self._c) / 3
        print(volume)
        return volume


# A sphere is considered to be a special type of ellipsoid, where are 3 diameters are equal
# So the class Sphere inherits from the Ellipsoid
class Sphere(Ellipsoid):

    def __init__(self, a):
        # TBD: why the parentheses here after super?
        super().__init__(a, a, a)


if __name__ == "__main__":
    Ellipsoid(1, 1, 1).calculate_volume()

    Sphere(1).calculate_volume()
