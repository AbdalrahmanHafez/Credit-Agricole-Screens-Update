import cv2
import pytesseract
import sys
from pytesseract import Output
from find_buttons import find_buttons, findRectangeNumber, getCenterOfButton

pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\dahom\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"


def proccess_info(data, filtered_box_ind, filename):
    # buttons pos is centerd, while nonbuttons are topleft
    result = {'buttons': {}, 'nonbuttons': {}}
    buttons_ind = find_buttons(filename)
    for i in filtered_box_ind:
        text = data['text'][i]
        loc_of_elm = (data['left'][i], data['top'][i])
        rec_of_loc_of_elm = findRectangeNumber(loc_of_elm[0], loc_of_elm[1])
        if(rec_of_loc_of_elm in buttons_ind):
            # text is inside a button
            # print("{} inside btn {}".format(text, rec_of_loc_of_elm))
            append = False
            if(str(rec_of_loc_of_elm) in result['buttons']):
                storedValue = result['buttons'][str(rec_of_loc_of_elm)]['text']
                append = True
            result['buttons'].update({str(rec_of_loc_of_elm): {
                'text': (((storedValue + " ") if append else "") + text), 'pos': getCenterOfButton(rec_of_loc_of_elm)}})
        else:
            # The button does not exists, text is not inside a button
            # print("{} not inside any btn".format(text))
            blocknum = data['block_num'][i]
            append = False
            if(str(blocknum) in result['nonbuttons']):
                storedValue = result['nonbuttons'][str(blocknum)]['text']
                append = True

            result['nonbuttons'].update(
                {str(blocknum): {'text': (((storedValue + " ") if append else "") + text), 'pos': loc_of_elm}})

    return result


def find_text(filename):
    img = cv2.imread(filename)
    orgImg = img.copy()
    # img = cv2.bitwise_not(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteImage) = cv2.threshold(
        grayImage, 140, 255, cv2.THRESH_BINARY)
    img = blackAndWhiteImage

    # hImg, wImg, _ = img.shape
    hImg, wImg = img.shape

    d = pytesseract.image_to_data(img, output_type=Output.DICT,
                                  config='-l eng+ara --oem 3 --tessdata-dir ./tessdata --psm 12 tessconfig')
    # print(d)

    n_boxes = len(d['level'])
    last_block_number = None
    filtered_box_ind = []
    for i in range(n_boxes):
        # Elimination stratigies
        confidence = d['conf'][i]

        if(confidence == "-1" or float(confidence) < 65):
            continue

        # Boxing separation
        # if(last_block_number and d['block_num'][i] != last_block_number):
            # print()
        last_block_number = d['block_num'][i]

        (x, y, w, h) = (d['left'][i], d['top']
                        [i], d['width'][i], d['height'][i])
        cv2.rectangle(orgImg, (x, y), (x + w, y + h), (0, 255, 0), 2)

        filtered_box_ind += [i]
        # print("B{:<3} conf={:<5} text={:<10} b#{} x={:<5} y={:<5} w={:<5} h={:<5}".format(
        #     i, confidence, d['text'][i], d['block_num'][i], x, y, w, h))
        # print("B{:<3} conf={:<5} text={:<10} b#{} W#={:<3} L#={:<3} par#={:<3}".format(
        # i, confidence, d['text'][i], d['block_num'][i], d['word_num'][i], d['line_num'][i], d['par_num'][i]))

    return proccess_info(d, filtered_box_ind, filename)

    # cv2.imshow('Result', orgImg)
    # # cv2.imshow('Result', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


# print(find_text(r"C:\Users\dahom\Desktop\ps_screen\input\Diball Screens.jpg"))
