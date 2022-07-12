from PGSettings import *
from ScoreTable import ScoreTable

scoreTab = ScoreTable()


def click_check(x, y):
    atLeastOneClick = False
    for obj in clickableObjects:
        if obj.if_clicked(x, y):
            atLeastOneClick = True
    return atLeastOneClick


def click_check_bool_only(x, y):
    atLeastOneClick = False
    for obj in clickableObjects:
        if obj.if_clicked_bool_only(x, y):
            atLeastOneClick = True
    return atLeastOneClick

def hex_light(hexa):
    oldFC = hexa.fillColor
    oldBC = hexa.borderColor
    c0 = hexa.fillColor[0]
    c1 = hexa.fillColor[1]
    c2 = hexa.fillColor[2]
    FC = [c0 - c0 / 3, c1 - c1 / 3, c2 - c2 / 3]
    hexa.set_colors(fillColor=FC, borderColor=WHITE)
    hexa.picture_show()
    hexa.set_colors(fillColor=oldFC, borderColor=oldBC)