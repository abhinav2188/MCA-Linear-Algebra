# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 01:49:44 2019

@author: abhi
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('img1.jpg',0)

#to autosize the image window
cv2.namedWindow('image',cv2.WINDOW_NORMAL)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('imgGray.jpg',img)