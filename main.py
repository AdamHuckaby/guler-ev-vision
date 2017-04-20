import cv2
import os

# Manually enter filename of pictures in ev_pics
pic_filename = 'Guler2-Dd2-g4-25_50kx.tif'

import numpy as np
from matplotlib import pyplot as plt

# Establish paths and directories for relevant files
source_dir = os.path.dirname(os.path.abspath(__file__))
pic_dir = os.sep.join([source_dir, 'ev_pics'])
pic_filepath = os.sep.join([pic_dir, pic_filename])

# Read in picture specified above
img = cv2.imread(pic_filepath, 0)
# blur_img =  cv2.GaussianBlur(img, (23), 0)


edges = cv2.Canny(img, 50, 200, 51)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()




# Always include at the end
# cv2.waitKey(0)