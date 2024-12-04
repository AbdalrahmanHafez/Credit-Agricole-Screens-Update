import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\dahom\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"

img = cv2.imread('ICON000.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# display(Image.fromarray(img))

# print(pytesseract.image_to_string(img, lang='eng+ara'))
hImg, wImg, _ = img.shape
# boxes = pytesseract.image_to_boxes(img, lang='eng+ara')
# for b in boxes.splitlines():
#     print(b)
#     b = b.split(' ')
#     x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
#     cv2.rectangle(img, (x, hImg-y), (w, hImg-h), (0, 0, 255), 1)
#     cv2.putText(img, b[0], (x, hImg-y+15),
#                 cv2.font, 1, (50, 50, 255))
config = r'--oem 3 --psm 3 lstmbox'
boxes = pytesseract.image_to_data(img, lang='eng+ara')
print(boxes)
for i, b in enumerate(boxes.splitlines()):
    if(i != 0):
        b = b.split()
        print(b)
        if(len(b) == 12):
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.rectangle(img, (x, y), (w+x, y+h), (0, 0, 255), 1)
            cv2.putText(img, b[11], (x, y),
                        cv2.FONT_HERSHEY_PLAIN, 1, (50, 50, 255))

cv2.imshow('Result', img)
cv2.waitKey(0)
