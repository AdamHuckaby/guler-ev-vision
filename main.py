# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 20:21:53 2017

@author: trave
"""


import cv2
import os

pic_filename = 'Guler2-Dd2-g4-25_50kx.tif'

source_dir = os.path.dirname(os.path.abspath(__file__))
pic_dir = os.sep.join([source_dir, 'ev_pics'])
pic_filepath = os.sep.join([pic_dir, pic_filename])


img = cv2.imread(pic_filepath)
img_small = cv2.resize(img, (600, 600))
blur_img = cv2.GaussianBlur(img_small, (25,25), 10)


cv2.namedWindow('Raw Image', cv2.WINDOW_NORMAL)
cv2.imshow('Raw Image', img)

cv2.imshow('Shrunk Image', img_small)
cv2.imshow('Blurry Image', blur_img)

cv2.waitKey(0)