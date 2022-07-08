from datetime import datetime
from zmq import Context, REQ
import numpy as np
import cv2 as cv


def shutdown(img, cords, color, bg):
    cv.circle(img, (10+cords[0], 25+cords[1]), 20, color, 3, lineType=cv.LINE_AA)
    cv.line(img, (10+cords[0], 25+cords[1]), (10+cords[0], 0+cords[1]), bg, 20)
    cv.line(img, (10+cords[0], 25+cords[1]), (10+cords[0], 0+cords[1]), color, 3, lineType=cv.LINE_AA)
    return img


def keyboard(img, cords, color):
    cv.rectangle(img, (0+cords[0], 0+cords[1]), (80+cords[0], 40+cords[1]), color, 3, lineType=cv.LINE_AA)
    cv.line(img, (10+cords[0], 10+cords[1]), (20+cords[0], 10+cords[1]), color, 3, lineType=cv.LINE_AA)
    cv.line(img, (30+cords[0], 10+cords[1]), (30+cords[0], 10+cords[1]), color, 3, lineType=cv.LINE_AA)
    cv.line(img, (40+cords[0], 10+cords[1]), (40+cords[0], 10+cords[1]), color, 3, lineType=cv.LINE_AA)
    cv.line(img, (50+cords[0], 10+cords[1]), (50+cords[0], 10+cords[1]), color, 3, lineType=cv.LINE_AA)
    cv.line(img, (60+cords[0], 10+cords[1]), (60+cords[0], 10+cords[1]), color, 3, lineType=cv.LINE_AA)
    cv.line(img, (70+cords[0], 10+cords[1]), (70+cords[0], 10+cords[1]), color, 3, lineType=cv.LINE_AA)
    cv.line(img, (10+cords[0], 20+cords[1]), (10+cords[0], 20+cords[1]), color, 3, lineType=cv.LINE_AA)
    cv.line(img, (20+cords[0], 20+cords[1]), (20+cords[0], 20+cords[1]), color, 3, lineType=cv.LINE_AA)
    cv.line(img, (30+cords[0], 20+cords[1]), (30+cords[0], 20+cords[1]), color, 3, lineType=cv.LINE_AA)
    cv.line(img, (40+cords[0], 20+cords[1]), (40+cords[0], 20+cords[1]), color, 3, lineType=cv.LINE_AA)
    cv.line(img, (50+cords[0], 20+cords[1]), (60+cords[0], 20+cords[1]), color, 3, lineType=cv.LINE_AA)
    cv.line(img, (70+cords[0], 20+cords[1]), (70+cords[0], 20+cords[1]), color, 3, lineType=cv.LINE_AA)
    cv.line(img, (10+cords[0], 30+cords[1]), (10+cords[0], 30+cords[1]), color, 3, lineType=cv.LINE_AA)
    cv.line(img, (20+cords[0], 30+cords[1]), (50+cords[0], 30+cords[1]), color, 3, lineType=cv.LINE_AA)
    cv.line(img, (60+cords[0], 30+cords[1]), (60+cords[0], 30+cords[1]), color, 3, lineType=cv.LINE_AA)
    cv.line(img, (70+cords[0], 30+cords[1]), (70+cords[0], 30+cords[1]), color, 3, lineType=cv.LINE_AA)
    return img


def slider_left(img, cords, color, bg):
    cv.circle(img, (16+cords[0], 16+cords[1]), 16, bg, -1, 16)
    cv.circle(img, (56+cords[0], 16+cords[1]), 16, bg, -1, 16)
    cv.rectangle(img, (16+cords[0], 0+cords[1]), (56+cords[0], 32+cords[1]), bg,-1, 16)
    cv.circle(img, (16+cords[0], 16+cords[1]), 12, color, -1, 16)
    return img


def slider_right(img, cords, color, bg):
    cv.circle(img, (16+cords[0], 16+cords[1]), 16, bg, -1, 16)
    cv.circle(img, (56+cords[0], 16+cords[1]), 16, bg, -1, 16)
    cv.rectangle(img, (16+cords[0], 0+cords[1]), (56+cords[0], 32+cords[1]), bg,-1, 16)
    cv.circle(img, (56+cords[0], 16+cords[1]), 12, color, -1, 16)
    return img


def global_menu(img, cords, color, border, bg, hover, settings, hovers):
    points = np.array([[0+cords[0], 0+cords[1]], [120+cords[0], 40+cords[1]], [120+cords[0], 440+cords[1]], [0+cords[0], 480+cords[1]]])
    cv.polylines(img, [points], True, border, 3, 16)
    cv.fillPoly(img, [points], bg, lineType=16)
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    date = now.strftime("%d-%m-%y")
    cv.putText(img, time, (3+cords[0], 80+cords[1]), 2, 0.8, color, 1, 16)
    cv.putText(img, date, (9+cords[0], 100+cords[1]), 2, 0.6, color, 1, 16)
    if settings["trail"] == "true":
        img = slider_right(img, (25+cords[0], 125+cords[1]), (255, 255, 255), (0, 200, 0))
    else:
        img = slider_left(img, (25+cords[0], 125+cords[1]), (255, 255, 255), (0, 0, 200))
    cv.putText(img, "Cursor Trail", (2+cords[0], 175+cords[1]), 2, 0.6, (0, 0, 0), 1, 16)

    points = np.array([[23+cords[0], 200+cords[1]], [23+cords[0], 220+cords[1]], [5+cords[0], 210+cords[1]]])
    if hovers[1]:
        cv.fillPoly(img, [points], hover, lineType=16)
    else:
        cv.fillPoly(img, [points], color, lineType=16)
    points = np.array([[97+cords[0], 200+cords[1]], [97+cords[0], 220+cords[1]], [115+cords[0], 210+cords[1]]])
    if hovers[2]:
        cv.fillPoly(img, [points], hover, lineType=16)
    else:
        cv.fillPoly(img, [points], color, lineType=16)

    text = cv.getTextSize(settings["background"][3:-4], 2, 0.7, 1)[0]
    cv.putText(img, settings["background"][3:-4], (int(60 - text[0] / 2)+cords[0], int(223 - text[1] / 2)+cords[1]), 2, 0.7, (0, 0, 0), 1, 16)

    if hovers[0]:
        img = shutdown(img, (50+cords[0], 378+cords[1]), hover, bg)
    else:
        img = shutdown(img, (50+cords[0], 378+cords[1]), color, bg)

    return img


def app(img, cords, icon, color):
    icon = cv.imread(f"/home/lualt/Lutetium/images/icon_{icon}.png")
    img[cords[0]:cords[0]+64, cords[1]:cords[1]+64] = icon

    return img
