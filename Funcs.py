import random
from colour import Color
import copy


def colorize(color):
    c0 = color[0] - int(color[0] * (random.randint(5, 30) / 100))
    c1 = color[1] - int(color[1] * (random.randint(5, 30) / 100))
    c2 = color[2] - int(color[2] * (random.randint(5, 30) / 100))
    resColor = (c0, c1, c2)
    return resColor


red = Color('red')
colorRange = list(red.range_to(Color(color='purple'), 19))
colorArray = copy.deepcopy(colorRange)
it = 0
step = 1
clickableObjects = []



def getRandColor():
    global colorArray
    if len(colorArray) == 0:
        colorArray = copy.deepcopy(colorRange)
        r = random.randint(0, len(colorArray) - 1)
        color = [colorArray[r].get_red() * 255, colorArray[r].get_green() * 255, colorArray[r].get_blue() * 255]
        colorArray.pop(r)
    else:
        r = random.randint(0, len(colorArray) - 1)
        color = [colorArray[r].get_red() * 255, colorArray[r].get_green() * 255, colorArray[r].get_blue() * 255]
        colorArray.pop(r)

    return color


def getRangedColor():
    global it
    color = [colorRange[it].get_red() * 255, colorRange[it].get_green() * 255, colorRange[it].get_blue() * 255]
    it += step
    it = it % 19
    return color





def noneFunc():
    return