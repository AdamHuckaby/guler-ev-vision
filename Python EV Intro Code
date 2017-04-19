# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 20:21:53 2017

@author: trave
"""


import cv2

img = cv2.imread('Guler6-Dd2pel-g4-25_50kx.tif')

img_small = cv2.resize(img, (600, 600))
blur_img = cv2.GaussianBlur(img_small, (25,25), 10)


#cv2.namedWindow('ASDF', cv2.WINDOW_NORMAL)
cv2.imshow('ASDF', blur_img)

cv2.waitKey(0)