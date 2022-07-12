from PGSettings import *
from Point import Point

class Edge:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def show(self, color=BLACK):
        pygame.draw.aaline(screen, color, [self.start.x, self.start.y], [self.end.x, self.end.y])

    def is_left(self, x, y):
        v1 = Point(self.end.x - x, self.end.y - y)
        v2 = Point(self.start.x - x, self.start.y - y)
        return (v1.y * v2.x) - (v1.x * v2.y) <= 0