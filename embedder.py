import cv2 as cv
import sys
import numpy as np

backgroundImg = cv.imread("background.png")
markerImg1 = cv.imread("marker_50.png")
markerImg2=cv.imread("marker_100.png")

x1 = int(input("First marker top left corner (x): "))
y1 = int(input("First marker top left corner (y): "))
x2 = int(input("Second marker top left corner (x): "))
y2 = int(input("Second marker top left corner (y): "))



roi_1 = backgroundImg[y1:y1+markerImg1.shape[0], x1:x1+markerImg1.shape[1]]
roi_2 = backgroundImg[y2:y2+markerImg2.shape[0], x2:x2+markerImg1.shape[1]]

overlay_alpha_1 = np.ones(markerImg1.shape[:2], dtype=np.float32)
overlay_alpha_2 = np.ones(markerImg2.shape[:2], dtype=np.float32)


roi_1[:] = markerImg1 * overlay_alpha_1[:, :, np.newaxis] + roi_1 * (1 - overlay_alpha_1[:, :, np.newaxis])
roi_2[:] = markerImg2 * overlay_alpha_2[:, :, np.newaxis] + roi_2 * (1 - overlay_alpha_2[:, :, np.newaxis])

cv.imwrite("shifted.png", backgroundImg)
cv.imshow("Result", backgroundImg)
cv.waitKey(0)
cv.destroyAllWindows()


