import cv2
import numpy as np

import sys

sys.setrecursionlimit(10 ** 9)

import selectinwindow

rectI = selectinwindow.dragRect

selectinwindow.init(rectI)

# REF
# http://www.pyimagesearch.com/2015/03/09/capturing-mouse-click-events-with-python-and-opencv/

# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not

I = np.ones([256, 256, 3], dtype=np.uint8)
I = I * 255
clone = I.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", selectinwindow.dragrect, rectI)

# keep looping until the 'q' key is pressed
while True:
    # display the image and wait for a keypress
    cv2.imshow("image", I)
    key = cv2.waitKey(1) & 0xFF

    # if the 'c' key is pressed, break from the loop
    if key == ord("c"):
        break

print str(rectI.outRect.x) + ',' + str(rectI.outRect.y) + ',' + \
      str(rectI.outRect.w) + ',' + str(rectI.outRect.h)


# close all open windows
# cv2.destroyAllWindows()
