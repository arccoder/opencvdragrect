import cv2
import numpy as np

import sys

# Set recursion limit
sys.setrecursionlimit(10 ** 9)

import selectinwindow

# Define the drag object
rectI = selectinwindow.dragRect

# Initialize the  drag object
imageWidth = 320
imageHeight = 240
image = np.ones([imageHeight, imageWidth, 3], dtype=np.uint8)
image *= 255
selectinwindow.init(rectI, image, imageWidth, imageHeight)

cv2.namedWindow("image")
cv2.setMouseCallback("image", selectinwindow.dragrect, rectI)

# keep looping until the 'q' key is pressed
while True:
    # display the image and wait for a keypress
    cv2.imshow("image", rectI.image)
    key = cv2.waitKey(1) & 0xFF

    # if the 'c' key is pressed, break from the loop
    if key == ord("c"):
        break

print str(rectI.outRect.x) + ',' + str(rectI.outRect.y) + ',' + \
      str(rectI.outRect.w) + ',' + str(rectI.outRect.h)

# close all open windows
cv2.destroyAllWindows()
