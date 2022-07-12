from PGSettings import *
from Funcs import *

class RectButton:
    def __init__(self, start, end, color, func=noneFunc, label=''):
        self.start = start
        self.end = end
        self.color = color
        self.width = self.end.x - self.start.x
        self.height = self.end.y - self.start.y
        self.func = func
        self.label = label

    def picture_show(self):
        pygame.draw.rect(screen, self.color, [self.start.x, self.start.y, self.width, self.height])
        labelText = lobster.render(self.label, False, (0, 0, 0))
        screen.blit(labelText, (self.start.x + self.width / 4, self.start.y + self.height / 3))
        # pygame.display.update()

    def show(self):
        self.picture_show()
        clickableObjects.append(self)

    def if_clicked(self, x, y):
        if (self.start.x <= x <= self.end.x) and (self.start.y <= y <= self.end.y):
            newColor = (255 - self.color[0], 255 - self.color[1], 255 - self.color[2])
            pygame.draw.rect(screen, newColor, [self.start.x, self.start.y, self.width, self.height])
            pygame.display.update()
            pygame.time.delay(50)  # ЕСЛИ КНОПКИ ПЛОХО РАБОТАЮТ УБРАТЬ ЭТО
            self.picture_show()  # ЕСЛИ КНОПКИ ПЛОХО РАБОТАЮТ УБРАТЬ ЭТО
            pygame.display.update()  # ЕСЛИ КНОПКИ ПЛОХО РАБОТАЮТ УБРАТЬ ЭТО
            self.func()
            return True
        else:
            self.picture_show()
            return

    def if_clicked_bool_only(self, x, y):
        if (self.start.x <= x <= self.end.x) and (self.start.y <= y <= self.end.y):
            return True
        else:
            return