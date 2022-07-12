from PGSettings import *
from Funcs import *
from Animation import Animation
from Point import Point
from Edge import Edge
from Hexagon import Hexagon
from RectButton import RectButton
from Level1 import Level1
from Level2 import Level2
from ScoreTable import ScoreTable
from Funcs2 import *


class MainMenu:
    def start(self):

        mainMenuRunning = True
        screen.fill(bgColor)
        helloFont = pygame.font.SysFont('Comic Sans MS', 50)
        helloText = helloFont.render('PySimon by maxim_tep', False, (0, 0, 0))
        screen.blit(helloText, (200, 100))

        pygame.display.update()
        while mainMenuRunning:
            screen.fill(bgColor)
            clickableObjects.clear()

            anim = Animation(Point(0, 0), Point(900, 650))
            anim.call(screen, WHITE)

            helloFont = pygame.font.SysFont('Comic Sans MS', 50)
            helloText = helloFont.render('PySimon by maxim_tep', False, (0, 0, 0))
            screen.blit(helloText, (200, 100))

            scoreTab.show()  # ТАБЛИЦА

            lvl1 = Level1(Point(550, 600))
            lvlButton1 = RectButton(Point(350, 200), Point(570, 300), HZ, label='Level 1', func=lvl1.startGame)
            lvlButton1.show()

            # lvl2 = Level2(Point(550, 600))
            lvlButton2 = RectButton(Point(350, 400), Point(570, 500), HZ, label='Level 2',
                                    func=Level2(Point(550, 600)).startGame)
            lvlButton2.show()

            mx = 0
            my = 0
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainMenuRunning = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx = int(event.pos[0])
                    my = int(event.pos[1])

            click_check(mx, my)
            pygame.display.update()



