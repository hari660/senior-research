import cv2 as cv
import sys
import numpy as np

backgroundImg = cv.imread("background.png")
markerImg = cv.imread("marker_50.png")

x,y=200,100

roi = backgroundImg[y:y+markerImg.shape[0], x:x+markerImg.shape[1]]

overlay_alpha = np.ones(markerImg.shape[:2], dtype=np.float32)

roi[:] = markerImg * overlay_alpha[:, :, np.newaxis] + roi * (1 - overlay_alpha[:, :, np.newaxis])

cv.imwrite("shifted.png", backgroundImg)
cv.imshow("Result", backgroundImg)
cv.waitKey(0)
cv.destroyAllWindows()


