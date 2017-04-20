import cv2
import os

# Manually enter filename of pictures in ev_pics
pic_filename = 'Guler2-Dd2-g4-25_50kx.tif'

# Establish paths and directories for relevant files
source_dir = os.path.dirname(os.path.abspath(__file__))
pic_dir = os.sep.join([source_dir, 'ev_pics'])
pic_filepath = os.sep.join([pic_dir, pic_filename])

# Read in picture specified above
img = cv2.imread(pic_filepath, 0)

# Shrink and blur the image
blur_window_size = 15
blur_img = cv2.GaussianBlur(img, (blur_window_size,)*2, 0)

threshold_value = 100
_, threshold_img = cv2.threshold(blur_img, threshold_value, 255, cv2.THRESH_BINARY)

#adaptThresh_img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 25, 2)
#adaptThresh_small = cv2.resize(adaptThresh_img, (800, 800))

# Show the raw image with a scalable window
cv2.namedWindow('Raw Image', cv2.WINDOW_NORMAL)
cv2.imshow('Raw Image', img)

# Show the small and blurred images with static windows
#cv2.imshow('Shrunk Image', img_small)
#cv2.imshow('Blurry Image', blur_img)

#cv2.imshow('Adaptive Threshold', adaptThresh_small)

cv2.namedWindow('Thresh Image', cv2.WINDOW_NORMAL)
cv2.imshow('Thresh Image', threshold_img)





# Always include at the end
cv2.waitKey(0)