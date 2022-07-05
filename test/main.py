from threading import Thread
from zmq import Context, REP
import numpy as np
import cv2 as cv

from system import config

# Public Variables
CURSOR = [-12, -12, 0]
FRAME = np.zeros((800, 480, 3), np.uint8)

# Global Variables
settings = {}
cursor = CURSOR.copy()
trail = []
frame = FRAME.copy()


# Functions
def tcp_server():
    global CURSOR, FRAME

    ctx = Context()
    sock = ctx.socket(REP)
    sock.bind("tcp://*:32123")

    while True:
        msg = sock.recv()
        if msg == b"get_cursor":
            sock.send(f"{CURSOR[0]} {CURSOR[1]} {CURSOR[2]}".encode())
        else:
            sock.send(b"")


def cursor_callback(event, x, y, *args):
    global cursor, trail

    cursor = [y, 480-x, event]


if __name__ == "__main__":
    cv.namedWindow("Lutetium", cv.WND_PROP_FULLSCREEN)
    cv.setWindowProperty("Lutetium", cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)
    cv.setMouseCallback("Lutetium", cursor_callback)

    tcp_thread = Thread(target=tcp_server, args=(), daemon=True)
    tcp_thread.start()

    settings = config.read()
    FRAME = cv.imread("/home/lualt/Lutetium/images/" + settings["background"])

    while True:
        img = FRAME.copy()
