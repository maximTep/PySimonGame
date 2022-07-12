from PGSettings import *

class Animation:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def call(self, screen, color):
        for i in range(200):
            rx = random.randint(self.start.x, self.end.x)
            ry = random.randint(self.start.y, self.end.y)
            pygame.draw.circle(screen, color, [rx, ry], 1)
        # pygame.display.update()