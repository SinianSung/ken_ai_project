import math


class Datapoint():

    def __init__(self, x, y, tag):
        self.x = x
        self.y = y
        self.tag = tag

    def __str__(self):
        return f"{round(self.x,4)}, {round(self.y,4)}, {self.tag}"

    def __repr__(self):
        return f"{round(self.x,4)}, {round(self.y,4)}, {self.tag}"

    def distance(self, x, y):
        dist_squared = (self.x - x)**2 + (self.y - y)**2
        return math.sqrt(dist_squared)

    def getTag(self):
        return self.tag
