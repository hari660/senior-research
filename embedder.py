import cv2 as cv
import sys
import numpy as np

backgroundImg = cv.imread("test.png")
markerImg = cv.imread("marker_50.png")

x,y=100,100

roi = backgroundImg[y:y+markerImg.shape[0], x:x+markerImg.shape[1]]

overlay_alpha = np.ones(markerImg.shape[:2], dtype=np.float32)

roi[:] = markerImg * overlay_alpha[:, :, np.newaxis] + roi * (1 - overlay_alpha[:, :, np.newaxis])

cv.imwrite("test_withmarker.png", backgroundImg)
cv.imshow("Result", backgroundImg)
cv.waitKey(0)
cv.destroyAllWindows()


