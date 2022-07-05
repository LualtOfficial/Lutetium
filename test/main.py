import numpy as np
import cv2 as cv

from system import config

# Public Variables
CURSOR = [0, -12, -12]
FRAME = np.zeros((800, 480, 3), np.uint8)

# Global Variables
settings = {}
cursor = [0, -12, -12]
trail = []


# Functions
def cursor_callback(event, x, y, *args):
    global cursor, trail

    cursor = [y, 480-x, event]


if __name__ == "__main__":
    cv.namedWindow("Lutetium", cv.WND_PROP_FULLSCREEN)
    cv.setWindowProperty("Lutetium", cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)

    settings = config.read("/home/lualt/Lutetium/system/settings.ini")
