from configparser import ConfigParser
from datetime import datetime
from time import sleep
from os import system
import numpy as np
import cv2 as cv
import keyboards
import icons


# Globabl Variables
cursor = [0, -12, -12]
old_cursor = [-12, -12]
menu = [-121, False]
trail = [[], True]
shutdown = False
config = ConfigParser()
backgrounds = [0, ["space", "sky", "logo"], False, False]


def mouse_callback(event, x, y, *args):
    global cursor, trail, menu, shutdown, old_cursor, backgrounds, background_img
    
    #print(cursor)
    
    # Cursor
    cursor = [event, y, 480-x]
    trail[0].append([y, 480-x])
    if len(trail[0]) > 30:
        del trail[0][0:len(trail) - 30]
    with open("/home/lualt/Lutetium/cursor", "w+") as file:
        if not menu[1]:
            file.write(f"{event}\n{x}\n{y}")
            old_cursor = [y, 480-x]
        else:
            file.write(f"0\n{old_cursor[0]}\n{old_cursor[1]}")
    
    # Menu Buttons Long Press
    if event == 2 and menu[0] == -1:
        # Shutdown
        if cursor[1] >= 37 and cursor[1] <= 82 and cursor[2] >= 381 and cursor[2] <= 421:
            test = system("sudo shutdown -h 0")
    # Menu Buttons Press
    if event == 4:
        # Trail Toggle
        if cursor[1] >= 25 and cursor[1] <= 96 and cursor[2] >= 126 and cursor[2] <= 153:
            trail[1] = not trail[1]
            config["DEFAULT"]["trail"] = "true" if trail[1] else "false"
            with open("/home/lualt/Lutetium/settings.ini", "w+") as file:
                config.write(file)
        if cursor[1] >= 37 and cursor[1] <= 82 and cursor[2] >= 381 and cursor[2] <= 421:
            exit()
        # Background Picker
        if cursor[1] >= 0 and cursor[1] <= 20 and cursor[2] >= 200 and cursor[2] <= 220:
            if backgrounds[0] == 0:
                backgrounds[0] = len(backgrounds[1]) - 1
                background_img = cv.imread(f"/home/lualt/Lutetium/bg_{backgrounds[1][backgrounds[0]]}.png", -1)
                config["DEFAULT"]["background"] = str(backgrounds[0])
                with open("/home/lualt/Lutetium/settings.ini", "w+") as file:
                    config.write(file)
            else:
                backgrounds[0] -= 1
                background_img = cv.imread(f"/home/lualt/Lutetium/bg_{backgrounds[1][backgrounds[0]]}.png", -1)
                config["DEFAULT"]["background"] = str(backgrounds[0])
                with open("/home/lualt/Lutetium/settings.ini", "w+") as file:
                    config.write(file)
        elif cursor[1] >= 100 and cursor[1] <= 120 and cursor[2] >= 200 and cursor[2] <= 220:
            if backgrounds[0] == len(backgrounds[1]) - 1:
                backgrounds[0] = 0
                background_img = cv.imread(f"/home/lualt/Lutetium/bg_{backgrounds[1][backgrounds[0]]}.png", -1)
                config["DEFAULT"]["background"] = str(backgrounds[0])
                with open("/home/lualt/Lutetium/settings.ini", "w+") as file:
                    config.write(file)
            else:
                backgrounds[0] += 1
                background_img = cv.imread(f"/home/lualt/Lutetium/bg_{backgrounds[1][backgrounds[0]]}.png", -1)
                config["DEFAULT"]["background"] = str(backgrounds[0])
                with open("/home/lualt/Lutetium/settings.ini", "w+") as file:
                    config.write(file)   
    # Menu Buttons Hover
        # Restart
    if cursor[1] >= 37 and cursor[1] <= 82 and cursor[2] >= 381 and cursor[2] <= 421:
        shutdown = True
    else:
        shutdown = False
    if cursor[1] >= 0 and cursor[1] <= 20 and cursor[2] >= 200 and cursor[2] <= 220:
        backgrounds[2] = True
    elif cursor[1] >= 100 and cursor[1] <= 120 and cursor[2] >= 200 and cursor[2] <= 220:
        backgrounds[3] = True
    else:
        backgrounds[2] = False
        backgrounds[3] = False
    
    # Show/Hide Menu
    if event == 2:
        menu[1] = not menu[1]


if __name__ == "__main__":
    cv.namedWindow("Lutetium", cv.WND_PROP_FULLSCREEN)
    cv.setWindowProperty("Lutetium", cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)
    cv.setMouseCallback("Lutetium", mouse_callback)
    
    config.read("/home/lualt/Lutetium/settings.ini")
    trail[1] = True if config["DEFAULT"]["trail"] == "true" else False
    backgrounds[0] = int(config["DEFAULT"]["background"])
    
    background_img = cv.imread(f"/home/lualt/Lutetium/bg_{backgrounds[1][backgrounds[0]]}.png", -1)
    blurred_frame = background_img.copy()
    
    while True:
        img = background_img.copy()
        
        #keyboards.numbers(img, (0, 320), (0, 0, 0), (245, 66, 90), (203, 245, 66))
        
        # Menu
            # Blur
        if menu[1] and menu[0] == -121:
            blurred_frame = cv.GaussianBlur(img, (31, 31), 0)
        if menu[1]:
            img = blurred_frame.copy()
            # Offset
        if menu[1] and menu[0] < -10:
            menu[0] += 10
        elif not menu[1] and menu[0] > -121:
            menu[0] -= 10
            # Shape
        points = np.array([[0+menu[0], 0], [120+menu[0], 40], [120+menu[0], 440], [0+menu[0], 480]])
        if menu[1]: cv.polylines(img, [points], True, (0, 0, 0), 3, 16)
        cv.fillPoly(img, [points], (223, 232, 60), lineType=16)
            # Time and Date
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        date = now.strftime("%d-%m-%y")
        cv.putText(img, time, (3+menu[0], 80), 2, 0.8, (0, 0, 0), 1, 16)
        cv.putText(img, date, (9+menu[0], 100), 2, 0.6, (0, 0, 0), 1, 16)
            # Trail toggle
        if trail[1]:
            img = icons.slider_right(img, (25+menu[0], 125), (255, 255, 255), (0, 200, 0))
        else:
            img = icons.slider_left(img, (25+menu[0], 125), (255, 255, 255), (0, 0, 200))
        cv.putText(img, "Cursor Trail", (2+menu[0], 175), 2, 0.6, (0, 0, 0), 1, 16)
            # Background Picker
        points = np.array([[23+menu[0], 200], [23+menu[0], 220], [5+menu[0], 210]])
        if backgrounds[2]:
            cv.fillPoly(img, [points], (150, 150, 150), lineType=16)
        else:
            cv.fillPoly(img, [points], (0, 0, 0), lineType=16)
        points = np.array([[97+menu[0], 200], [97+menu[0], 220], [115+menu[0], 210]])
        if backgrounds[3]:
            cv.fillPoly(img, [points], (150, 150, 150), lineType=16)
        else:
            cv.fillPoly(img, [points], (0, 0, 0), lineType=16)
        text = cv.getTextSize(backgrounds[1][backgrounds[0]], 2, 0.7, 1)[0]
        cv.putText(img, backgrounds[1][backgrounds[0]], (int(60 - text[0]/2)+menu[0], int(223 - text[1]/2)), 2, 0.7, (0, 0, 0), 1, 16)
            # Shutdown and Restart
        if shutdown:
            img = icons.shutdown(img, (50+menu[0], 378), (150, 150, 150), (223, 232, 60))
        else:
            img = icons.shutdown(img, (50+menu[0], 378), (0, 0, 0), (223, 232, 60))
        
        
        
        # Trail
        if trail[1]:
            points = np.array(trail[0], np.int32)
            cv.polylines(img, [points], False, (0, 0, 0), 3, 16)
            cv.polylines(img, [points], False, (255, 255, 255), 1, 16)
    
        # Cursor
        cv.circle(img, (cursor[1], cursor[2]), 12, (0, 0, 0), -1, 16)
        cv.circle(img, (cursor[1], cursor[2]), 10, (255, 255, 255), -1, 16)
        
        img = cv.rotate(img, 0)
        cv.imshow("Lutetium", img)
        cv.waitKey(1)
