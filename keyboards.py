from threading import Thread
import cv2 as cv

keys = []


def thread():
    global keys
    with open("/home/lualt/Lutetium/cursor", "r") as file:
        while len(keys) >= 1:
            cursor = file.readlines()
            for key in keys:
                try:
                    if int(cursor[1]) >= key[0] and int(cursor[1]) <= key[0]+80 and int(cursor[2]) >= key[1] and int(cursor[2]) <= key[1]+40:
                        print("Pressed key", key[2])
                except IndexError:
                    pass

def activate():
# fuck me you have to optimise this future me
    global keys
    if len(keys) >= 1:
        Thread(target=thread, args=(), daemon=True).start()


def key(img, char, cords, color, border, bg):
    cv.rectangle(img, (0+cords[0], 0+cords[1]), (80+cords[0], 40+cords[1]), bg, -1)
    cv.rectangle(img, (0+cords[0], 0+cords[1]), (80+cords[0], 40+cords[1]), border, 1, 16)
    cv.putText(img, char, (30+cords[0], 30+cords[1]), 2, 1, color, 1, 16)
    keys.append((cords[0], cords[1], char))
    return img
    
def numbers(img, cords, color, border, bg):
    cv.rectangle(img, (0+cords[0], 0+cords[1]), (800+cords[0], 160+cords[1]), bg, -1)
    cv.rectangle(img, (0+cords[0], 0+cords[1]), (799+cords[0], 159+cords[1]), border, 1, 16)
    img = key(img, "0", (360+cords[0], 120+cords[1]), (0, 0, 0), (245, 66, 90), (203, 245, 66))
    img = key(img, "1", (280+cords[0], 80+cords[1]), (0, 0, 0), (245, 66, 90), (203, 245, 66))
    img = key(img, "2", (360+cords[0], 80+cords[1]), (0, 0, 0), (245, 66, 90), (203, 245, 66))
    img = key(img, "3", (440+cords[0], 80+cords[1]), (0, 0, 0), (245, 66, 90), (203, 245, 66))
    img = key(img, "4", (280+cords[0], 40+cords[1]), (0, 0, 0), (245, 66, 90), (203, 245, 66))
    img = key(img, "5", (360+cords[0], 40+cords[1]), (0, 0, 0), (245, 66, 90), (203, 245, 66))
    img = key(img, "6", (440+cords[0], 40+cords[1]), (0, 0, 0), (245, 66, 90), (203, 245, 66))
    img = key(img, "7", (280+cords[0], 0+cords[1]), (0, 0, 0), (245, 66, 90), (203, 245, 66))
    img = key(img, "8", (360+cords[0], 0+cords[1]), (0, 0, 0), (245, 66, 90), (203, 245, 66))
    img = key(img, "9", (440+cords[0], 0+cords[1]), (0, 0, 0), (245, 66, 90), (203, 245, 66))
    img = key(img, "v", (540+cords[0], 20+cords[1]), (0, 0, 0), (245, 66, 90), (203, 245, 66))
    img = key(img, "x", (540+cords[0], 60+cords[1]), (0, 0, 0), (245, 66, 90), (203, 245, 66))
    return img