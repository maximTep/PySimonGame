from PGSettings import *
from Funcs import *
from Point import Point
from Edge import Edge

class Hexagon:
    def __init__(self, initPos, borderColor=BLACK, fillColor=WHITE, func=noneFunc):
        self.pos = initPos
        self.edges = []
        self.edgeSize = 70
        self.borderColor = borderColor
        self.fillColor = fillColor
        self.func = noneFunc

        edgeEnd = Point(initPos.x + self.edgeSize * math.sqrt(3) / 2,  # self.edgeSize/2
                        initPos.y - self.edgeSize / 2)  # self.edgeSize*math.sqrt(3)/2
        self.edges.append(Edge(initPos, edgeEnd))
        edgeEnd = Point(self.edges[-1].end.x, self.edges[-1].end.y - self.edgeSize)
        self.edges.append(Edge(self.edges[-1].end, edgeEnd))
        edgeEnd = Point(self.edges[-1].end.x - self.edgeSize * math.sqrt(3) / 2,
                        self.edges[-1].end.y - self.edgeSize / 2)
        self.edges.append(Edge(self.edges[-1].end, edgeEnd))
        edgeEnd = Point(self.edges[-1].end.x - self.edgeSize * math.sqrt(3) / 2,
                        self.edges[-1].end.y + self.edgeSize / 2)
        self.edges.append(Edge(self.edges[-1].end, edgeEnd))
        edgeEnd = Point(self.edges[-1].end.x, self.edges[-1].end.y + self.edgeSize)
        self.edges.append(Edge(self.edges[-1].end, edgeEnd))
        edgeEnd = Point(self.edges[-1].end.x + self.edgeSize * math.sqrt(3) / 2,
                        self.edges[-1].end.y + self.edgeSize / 2)
        self.edges.append(Edge(self.edges[-1].end, edgeEnd))
        self.func = func

    def set_colors(self, borderColor=BLACK, fillColor=WHITE):
        self.borderColor = borderColor
        self.fillColor = fillColor

    def picture_show(self):
        points = [[i.start.x, i.start.y] for i in self.edges]
        pygame.draw.polygon(screen, self.fillColor, points)
        pygame.draw.aalines(screen, self.fillColor, True, points)
        for i in self.edges:
            i.show(self.borderColor)
        pygame.display.update()

    def show(self):
        self.picture_show()
        clickableObjects.append(self)

    def if_clicked(self, x, y):
        for edge in self.edges:
            if not edge.is_left(x, y):
                self.picture_show()
                return
        if self.func != noneFunc:
            self.func(self)
        return True

    def if_clicked_bool_only(self, x, y):
        for edge in self.edges:
            if not edge.is_left(x, y):
                return
        if self.func != noneFunc:
            pass
        return True

    def click(self):
        self.if_clicked(self.pos.x, self.pos.y)