import pygame
import random
import pygame
from tkinter import *
from tkinter import messagebox
import math
import datetime
from Funcs import *


pygame.init()
pygame.font.init()
myFont = pygame.font.SysFont('Comic Sans MS', 30)
lobster = pygame.font.SysFont('Lobster Regular 400', 50)
screenWidth = 900
screenHeight = 650
screen = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption("Simon")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
MAGENTA = (255, 0, 255)
CYAN = (255, 255, 0)
YELLOW = (0, 255, 255)
ORANGE = (255, 91, 0)
HZ = (100, 100, 100)
colors = [RED, GREEN, BLUE, CYAN, MAGENTA, YELLOW]
randomizedColors = [(random.randint(30, 255), random.randint(30, 255), random.randint(30, 255))
                    for i in range(100)]



running = True
bgColor = colorize(colorize((colorize(YELLOW))))
# screen.fill(bgColor)
bgImage = pygame.image.load('SimonBG.jpg')

