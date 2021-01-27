# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 19:14:45 2019

@author: MAHE
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 09:01:32 2019

@author: MAHE
"""

# import the necessary packages
from PIL import Image
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
#import argparse
import cv2
import os
import numpy as np
from pytesseract import Output

image = cv2.imread('D:\Animish\coin_crop\polar_crop3.jpg',0)
#image = cv2.resize(image,(1500,150))
#img2 = cv2.resize(img,(500,500))

#gray = cv2.medianBlur(image,9)
#gray = cv2.threshold(image, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
gray = cv2.threshold(image, 180,255, cv2.THRESH_TOZERO)[1]

'''
kernelero = np.ones((2,2),np.uint8)
kerneldil = np.ones((3,3),np.uint8)
kernelopen = np.ones((2,2),np.uint8)
kernelclose = np.ones((6,6),np.uint8)
#gray = cv2.dilate(gray,kerneldil,iterations = 2)

gray = cv2.erode(gray,kernelero,iterations = 1)

gray = cv2.dilate(gray,kerneldil,iterations = 2)
gray = cv2.medianBlur(gray,9)
'''
'''
kernelclose = np.ones((2,2),np.uint8)
gray = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernelclose)
kernelopen = np.ones((2,2),np.uint8)
gray = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernelopen)
kerneldil = np.ones((2,2),np.uint8)
gray = cv2.dilate(gray,kerneldil,iterations = 1)
'''
'''
gray = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernelopen)

gray = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernelclose)
gray = cv2.dilate(gray,kerneldil,iterations = 2)
#gray = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernelclose)
'''
filename = "D:\Animish\coin_crop\{}.jpg".format(os.getpid())

cv2.imwrite(filename, gray)


pytesseract.pytesseract.tesseract_cmd = r'C:\Users\MAHE\AppData\Local\Tesseract-OCR\tesseract.exe'

text = pytesseract.image_to_boxes(Image.open(filename))

#os.remove(filename)

print(text)
d = pytesseract.image_to_data(gray, output_type=Output.DICT)
n_boxes = len(d['level'])
for i in range(n_boxes):
    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
    cv2.rectangle(gray, (x, y), (x + w, y + h), (255, 255, 255), 2)

cv2.imshow('img', gray)
cv2.waitKey(0)
#im = Image.open("temp.jpg")
