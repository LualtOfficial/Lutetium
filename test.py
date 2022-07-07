from zmq import Context, REQ
import numpy as np
import cv2 as cv

ctx = Context()
sock = ctx.socket(REQ)
sock.connect("tcp://localhost:32123")

img = np.zeros((480, 800, 3), np.uint8)
cv.putText(img, "Test", (50, 50), 2, 0.8, (255, 255, 255), 1, 16)
cursor = (-12, -12, 0)

while True:
    sock.send(b"get_cursor")
    resp = sock.recv().decode().split(" ")
    cursor = (int(resp[0]), int(resp[1]), int(resp[2]))

    cv.circle(img, (cursor[0], cursor[1]), 16, (150, 150, 150), -1, 16)

    sock.send(b"set_frame")
    if sock.recv() == b"1":
        sock.send(img.tobytes())
        sock.recv()
