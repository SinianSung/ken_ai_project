import math


class Datapoint():

    def __init__(self, x, y, z, tag):
        self.x = x
        self.y = y
        self.z = z
        self.tag = tag

    def __str__(self):
        return f"{self.x}, {self.y}, {self.z}, {self.tag}"

    def __repr__(self):
        return f"{self.x}, {self.y}, {self.z}, {self.tag}"

    def distance(self, other):
        abstand = (self.x-other.x)**2 + \
            (self.y-other.y)**2 + (self.z-other.z)**2
        return math.sqrt(abstand)
