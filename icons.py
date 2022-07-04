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
