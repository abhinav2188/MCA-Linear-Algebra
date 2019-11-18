# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 01:49:44 2019

@author: abhi
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2

#reading image in grayscale
img = cv2.imread('img1.jpg',0)

#to autosize the image window
cv2.namedWindow('image',cv2.WINDOW_NORMAL)

cv2.imshow('image',img)

#to wait for a key press to exit the image window
cv2.waitKey(0)
cv2.destroyAllWindows()

#to write the grayscale image into new file
cv2.imwrite('imgGray.jpg',img)

pixel = img[100,100]

img_negative = cv2.bitwise_not(img)



cv2.imshow('image',img_negative)

#to wait for a key press to exit the image window
cv2.waitKey(0)
cv2.destroyAllWindows()
