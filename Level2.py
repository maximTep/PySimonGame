from  PGSettings import *
from Hexagon import Hexagon
from Point import Point
from Funcs2 import *
from RectButton import RectButton


class Level2:
    def __init__(self, initPos):
        self.hexs = []
        positions = []
        positions.append(initPos)
        self.hexs.append(Hexagon(positions[-1]))
        positions.append(self.hexs[0].edges[3].end)
        self.hexs.append(Hexagon(positions[-1]))
        positions.append(self.hexs[0].edges[1].end)
        self.hexs.append(Hexagon(positions[-1]))
        positions.append(self.hexs[1].edges[3].end)
        self.hexs.append(Hexagon(positions[-1]))
        positions.append(self.hexs[1].edges[1].end)
        self.hexs.append(Hexagon(positions[-1]))
        positions.append(self.hexs[2].edges[1].end)
        self.hexs.append(Hexagon(positions[-1]))
        positions.append(self.hexs[4].edges[3].end)
        self.hexs.append(Hexagon(positions[-1]))
        positions.append(self.hexs[4].edges[1].end)
        self.hexs.append(Hexagon(positions[-1]))

        distX = self.hexs[0].edgeSize * math.sqrt(3) / 2
        distY = self.hexs[0].edgeSize / 2

        positions.append(Point(self.hexs[0].pos.x - 2 * distX, self.hexs[0].pos.y))
        positions.append(Point(self.hexs[0].pos.x - 3 * distX, self.hexs[0].pos.y - 3 * distY))
        positions.append(Point(self.hexs[0].pos.x - 4 * distX, self.hexs[0].pos.y - 6 * distY))
        positions.append(Point(self.hexs[0].pos.x - 3 * distX, self.hexs[0].pos.y - 9 * distY))
        positions.append(Point(self.hexs[0].pos.x - 2 * distX, self.hexs[0].pos.y - 12 * distY))
        positions.append(Point(self.hexs[0].pos.x, self.hexs[0].pos.y - 12 * distY))

        positions.append(Point(self.hexs[0].pos.x + 3 * distX, self.hexs[0].pos.y - 3 * distY))
        positions.append(Point(self.hexs[0].pos.x + 2 * distX, self.hexs[0].pos.y))
        positions.append(Point(self.hexs[0].pos.x + 4 * distX, self.hexs[0].pos.y - 6 * distY))
        positions.append(Point(self.hexs[0].pos.x + 3 * distX, self.hexs[0].pos.y - 9 * distY))
        positions.append(Point(self.hexs[0].pos.x + 2 * distX, self.hexs[0].pos.y - 12 * distY))

        self.hexs.clear()
        # positions.pop(0)
        # randColors = [RED, GREEN, BLUE, CYAN, MAGENTA, YELLOW, ORANGE]
        # randColors = copy.deepcopy(randomizedColors)
        ite = 0
        step = 10000
        for newPos in positions:
            color = getRangedColor()
            self.hexs.append(Hexagon(newPos, fillColor=color, func=hex_light))
        for hexa in self.hexs:
            pass  # hexa.show()

    def show(self):
        for hex in self.hexs:
            hex.show()

    def startGame(self):
        seq = []
        userColorsSeq = []
        rightColorSeq = []
        score = 0
        playerTurn = False
        playing = True
        screen.blit(bgImage, (200, 0))
        for obj in clickableObjects:
            if isinstance(obj, RectButton):
                clickableObjects.pop(clickableObjects.index(obj))
        for obj in clickableObjects:
            if isinstance(obj, RectButton):
                clickableObjects.pop(clickableObjects.index(obj))
        while playing:
            pygame.draw.rect(screen, bgColor, [0, 0, 200, screenHeight])
            textSurface = myFont.render('Score: ' + str(score), False, (0, 0, 0))
            screen.blit(textSurface, (30, 10))
            for hex in self.hexs:
                hex.show()
            mx = 0
            my = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit(0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx = int(event.pos[0])
                    my = int(event.pos[1])

            if playerTurn:
                for i in seq:
                    mx = 0
                    my = 0
                    click_check(mx, my)
                    wasClicked = False
                    while not wasClicked:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                exit(0)
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                mx = int(event.pos[0])
                                my = int(event.pos[1])
                        wasClicked = click_check_bool_only(mx, my)

                    for j in range(len(self.hexs)):
                        if self.hexs[j].if_clicked(mx, my):
                            userColorsSeq.append(self.hexs[j].fillColor)
                            pygame.time.delay(200)
                            if i != j:
                                playing = False
                                # print(score)
                                Tk().wm_withdraw()
                                messagebox.showinfo('', 'You\'ve lost with ' + str(score) + ' points.')
                                scoreTab.add_note(score, 2, userColorsSeq, rightColorSeq)
                                return
                                # exit(0)
                score += 1
                playerTurn = False
                self.show()
                pygame.time.delay(700)

            else:
                pygame.time.delay(1000)
                seq.append(random.randint(0, len(self.hexs) - 1))
                newSeq = [random.randint(0, len(self.hexs) - 1) for i in range(len(seq))]
                seq = newSeq
                rightColorSeq.append(self.hexs[seq[-1]].fillColor)
                for i in seq:
                    self.hexs[i].click()
                    pygame.display.update()
                    pygame.time.delay(500)
                    self.hexs[i].picture_show()
                    pygame.display.update()
                    pygame.time.delay(500)
                playerTurn = True
                pygame.time.delay(0)

            pygame.display.update()