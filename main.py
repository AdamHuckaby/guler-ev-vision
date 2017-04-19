import cv2
import os

# Manually enter filename of pictures in ev_pics
pic_filename = 'Guler2-Dd2-g4-25_50kx.tif'

# Establish paths and directories for relevant files
source_dir = os.path.dirname(os.path.abspath(__file__))
pic_dir = os.sep.join([source_dir, 'ev_pics'])
pic_filepath = os.sep.join([pic_dir, pic_filename])

# Read in picture specified above
img = cv2.imread(pic_filepath)

# Shrink and blur the image
img_small = cv2.resize(img, (600, 600))
blur_img = cv2.GaussianBlur(img_small, (25,25), 10)

# Show the raw image with a scalable window
cv2.namedWindow('Raw Image', cv2.WINDOW_NORMAL)
cv2.imshow('Raw Image', img)

# Show the small and blurred images with static windows
cv2.imshow('Shrunk Image', img_small)
cv2.imshow('Blurry Image', blur_img)


# Always include at the end
cv2.waitKey(0)