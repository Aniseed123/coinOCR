# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 09:31:18 2019

@author: MAHE
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
img = cv2.imread('D:\Animish\coin_crop\FiveRe_1.jpg',0)

#img2 = cv2.resize(img,(500,500))
polar = cv2.logPolar(img2, (250,250),80, cv2.WARP_FILL_OUTLIERS )
rotated = cv2.rotate(polar, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow('image',rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()