from os import system, listdir
from threading import Thread
from zmq import Context, REP
import numpy as np
import cv2 as cv

from system import config
from system import graphics

# Public Variables
CURSOR = [-12, -12, 0]
FRAME = np.zeros((800, 480, 3), np.uint8)

# Global Variables
settings = {}
cursor = CURSOR.copy()
trail = []
menu = [False, -120]
hover = [False, False, False]
backgrounds = [0, ["bg_space.png"]]


# Functions
def tcp_server():
    global CURSOR, FRAME

    ctx = Context()
    sock = ctx.socket(REP)
    sock.bind("tcp://*:32123")

    while True:
        msg = sock.recv()
        if msg == b"get_cursor":
            sock.send(" ".join([str(num) for num in CURSOR]).encode())
        elif msg == b"set_frame":
            sock.send(b"1")
            resp = sock.recv()
            if not menu[0]:
                FRAME = np.frombuffer(resp, dtype=np.uint8).reshape((480, 800, 3))
            sock.send(b"1")
        else:
            sock.send(b"0")


def cursor_callback(event, x, y, *_):
    global cursor, trail, settings, CURSOR, hover, FRAME, backgrounds

    cursor = [y, 480-x, event]

    if not menu[0]:
        CURSOR = cursor
    if settings["trail"]:
        trail.append([cursor[0], cursor[1]])
        del trail[0:len(trail) - 30]

    if event == 2:
        menu[0] = not menu[0]
        if menu[0] == 0 and 37 <= cursor[0] <= 82 and 381 <= cursor[1] <= 421:
            system("sudo shutdown -h 0")

    hover = [False]*len(hover)
    if 37 <= cursor[0] <= 82 and 381 <= cursor[1] <= 421:
        hover[0] = True
    elif 0 <= cursor[0] <= 20 and 200 <= cursor[1] <= 220:
        hover[1] = True
    elif 100 <= cursor[0] <= 120 and 200 <= cursor[1] <= 220:
        hover[2] = True

    if event == 4:
        if 25 <= cursor[0] <= 96 and 126 <= cursor[1] <= 153:
            settings["trail"] = "false" if settings["trail"] == "true" else "true"
            config.write(settings)
        elif 37 <= cursor[0] <= 82 and 381 <= cursor[1] <= 421:
            exit()
        elif 0 <= cursor[0] <= 20 and 200 <= cursor[1] <= 220:
            backgrounds[1].clear()
            for bg_img in listdir("/home/lualt/Lutetium/images/"):
                if bg_img[:3] == "bg_":
                    backgrounds[1].append(bg_img)
            backgrounds[0] = backgrounds[1].index(settings["background"])
            if backgrounds[0] == 0:
                backgrounds[0] = len(backgrounds[1]) - 1
            else:
                backgrounds[0] -= 1
            settings["background"] = backgrounds[1][backgrounds[0]]
            config.write(settings)
            FRAME = cv.GaussianBlur(cv.imread("/home/lualt/Lutetium/images/" + settings["background"]), (31, 31), 0)
        elif 100 <= cursor[0] <= 120 and 200 <= cursor[1] <= 220:
            backgrounds[1].clear()
            for bg_img in listdir("/home/lualt/Lutetium/images/"):
                if bg_img[:3] == "bg_":
                    backgrounds[1].append(bg_img)
            backgrounds[0] = backgrounds[1].index(settings["background"])
            if backgrounds[0] == len(backgrounds[1]) - 1:
                backgrounds[0] = 0
            else:
                backgrounds[0] += 1
            settings["background"] = backgrounds[1][backgrounds[0]]
            config.write(settings)
            FRAME = cv.GaussianBlur(cv.imread("/home/lualt/Lutetium/images/" + settings["background"]), (31, 31), 0)


if __name__ == "__main__":
    cv.namedWindow("Lutetium", cv.WND_PROP_FULLSCREEN)
    cv.setWindowProperty("Lutetium", cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)
    cv.setMouseCallback("Lutetium", cursor_callback)

    tcp_thread = Thread(target=tcp_server, args=())
    tcp_thread.daemon = True
    tcp_thread.start()

    settings = config.read()
    for bg_img in listdir("/home/lualt/Lutetium/images/"):
        if bg_img[:3] == "bg_" and bg_img != "bg_space.png":
            backgrounds[1].append(bg_img)
    backgrounds[0] = backgrounds[1].index(settings["background"])
    FRAME = cv.imread("/home/lualt/Lutetium/images/" + settings["background"])

    while True:
        img = FRAME.copy()

        img = graphics.app(img, (100, 100), "test", (255, 255, 255))

        if menu[0] and menu[1] == -120:
            FRAME = cv.GaussianBlur(FRAME, (31, 31), 0)
        elif not menu[0] and menu[1] == 0:
            FRAME = cv.imread("/home/lualt/Lutetium/images/" + settings["background"])
        if menu[0] and menu[1] != 0:
            menu[1] += 10
        elif not menu[0] and menu[1] != -120:
            menu[1] -= 10

        if menu[1] != -120:
            img = graphics.global_menu(img, (menu[1], 0), (0, 0, 0), (0, 0, 0), (233, 232, 60), (150, 150, 150), settings, hover)

        if settings["trail"] == "true":
            points = np.array(trail, np.int32)
            cv.polylines(img, [points], False, (0, 0, 0), 3, 16)
            cv.polylines(img, [points], False, (255, 255, 255), 1, 16)

        cv.circle(img, (cursor[0], cursor[1]), 12, (0, 0, 0), 2, 16)
        cv.circle(img, (cursor[0], cursor[1]), 10, (255, 255, 255), -1, 16)

        img = cv.rotate(img, 0)
        cv.imshow("Lutetium", img)
        cv.waitKey(1)
