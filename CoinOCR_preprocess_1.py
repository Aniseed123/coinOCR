# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 08:40:09 2019

@author: MAHE
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
img = cv2.imread('D:\Animish\America_1.jpg',0)

imgcol = cv2.imread('D:\Animish\America_1.jpg',1)
#imgcol = cv2.resize(img,(720,960))

#img2 = cv2.resize(img,(720,960))  #(720,960)

img3 = cv2.medianBlur(img,9)
cimg = cv2.cvtColor(img3,cv2.COLOR_GRAY2BGR)
circles = cv2.HoughCircles(img3,cv2.HOUGH_GRADIENT,1,100,
                            param1=100,param2=50,minRadius=0,maxRadius=200)
circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
'''
cv2.imshow('detected circles',imgcol)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

for i in circles[0,:]:
    x = i[0]
    y = i[1]
    r = i[2]
    rectX = (x - r) 
    rectY = (y - r)
    crop_img = imgcol[rectY-2:(rectY+2*r)+2, rectX-2:(rectX+2*r)+2]
    #polar = cv2.logPolar(crop_img, (x,y),80, cv2.WARP_FILL_OUTLIERS )
    #polar2= cv2.LogPolar(crop_img,)
    crop_img = cv2.resize(crop_img,(500,500))
    polar = cv2.logPolar(crop_img, (250,250),80, cv2.WARP_FILL_OUTLIERS )
    rotated = cv2.rotate(polar, cv2.ROTATE_90_COUNTERCLOCKWISE)
    #cv2.imwrite("D:\Animish\coin_crop\Trial2\coin-{:03d}.jpg".format(i[0]), crop_img)
    #cv2.imwrite("D:\Animish\coin_crop\Trial2\coin-{:03d}-polar.jpg".format(i[0]), rotated)
    snip_img = rotated[60:100,0:500]
    snip_img= cv2.resize(snip_img,(1500,150))
    #cv2.imwrite("D:\Animish\coin_crop\Trial2\coin-{:03d}-polarsnip.jpg".format(i[0]), snip_img)
    gray = cv2.threshold(snip_img, 180,255, cv2.THRESH_TOZERO)[1]
    cv2.imwrite("D:\Animish\coin_crop\preprocess 1\coin-{:03d}-polarsnip.jpg".format(i[0]), gray)
   