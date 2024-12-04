# please make sure that the template button.jpg is present
import cv2
import pytesseract
import numpy as np
from imutils.object_detection import non_max_suppression

pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\dahom\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"


def getCenterOfButton(btnNumber):
    def calcCenter(x, y):
        tw = 289
        th = 49
        return (x+tw/2, y+th/2)

    if(btnNumber == 1):
        return calcCenter(9, 163)
    if(btnNumber == 2):
        return calcCenter(345, 163)
    if(btnNumber == 3):
        return calcCenter(9, 246)
    if(btnNumber == 4):
        return calcCenter(345, 246)
    if(btnNumber == 5):
        return calcCenter(9, 336)
    if(btnNumber == 6):
        return calcCenter(345, 336)
    if(btnNumber == 7):
        return calcCenter(9, 418)
    if(btnNumber == 8):
        return calcCenter(345, 418)


def findRectangeNumber(x, y):
    def insideBox(point, x, y):
        threshold = 10
        tw = 289
        th = 49
        topleft = (x - threshold, y - threshold)
        botright = (x + tw + threshold, y + th + threshold)
        return (
            (topleft[0] < point[0] < botright[0])
            and
            (topleft[1] < point[1] < botright[1])
        )
        #  1. p0 x coordinate < point x < p1 x coordinate
        #  2. p0 y coordinate < point y < p1 y coordinate

    point = (x, y)

    if(insideBox(point, 9, 163)):
        return 1
    if(insideBox(point, 345, 163)):
        return 2
    if(insideBox(point, 9, 246)):
        return 3
    if(insideBox(point, 345, 246)):
        return 4
    if(insideBox(point, 9, 336)):
        return 5
    if(insideBox(point, 345, 336)):
        return 6
    if(insideBox(point, 9, 418)):
        return 7
    if(insideBox(point, 345, 418)):
        return 8
    return 0


def find_buttons(filename):
    imgBtn = cv2.imread('button.jpg')
    img = cv2.imread(filename)
    imageBtnGray = cv2.cvtColor(imgBtn, cv2.COLOR_BGR2GRAY)
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # img = cv2.imread('buttons_grid.jpg', 0)

    hImg, wImg = imgBtn.shape[:2]

    img2 = imgGray.copy()
    convResult = cv2.matchTemplate(imgGray, imageBtnGray, cv2.TM_CCOEFF_NORMED)
    # dim of (W - w +1, H -h +1)
    # min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(convResult)
    (yCoords, xCoords) = np.where(convResult >= 0.5)
    # print(min_loc, max_loc, str(method))
    # if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
    #     location = min_loc
    # else:
    #     location = max_loc
    # bottom_right = (location[0] + wImg, location[1] + hImg)
    # cv2.rectangle(img2, location, bottom_right, (0, 150, 255), 1)

    # loop over our starting (x, y)-coordinates
    rects = []

    for (x, y) in zip(xCoords, yCoords):
        # draw the bounding box on the image
        rects.append((x, y, x + wImg, y + hImg))
        # cv2.rectangle(img2, (x, y), (x + wImg, y + hImg),  (0, 150, 255), 1)

    pick = non_max_suppression(np.array(rects))

    # loop over the final bounding boxes

    found_buttons = []
    for (startX, startY, endX, endY) in pick:
        # print(startX, startY)
        found = findRectangeNumber(startX, startY)
        if(found != 0):
            found_buttons += [found]
        # draw the bounding box on the image
        cv2.rectangle(img2, (startX, startY), (endX, endY),	(0, 150, 255), 2)

    return found_buttons
    # cv2.imshow('match', img2)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
