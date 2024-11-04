import cv2
import numpy as np

# Load the image
image = cv2.imread('test_withmarker.png')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
parameters = cv2.aruco.DetectorParameters()

# Create the ArUco detector
detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)
# Detect the markers
corners, ids, rejected = detector.detectMarkers(gray)
newCorners = [[int(i) for i in j] for j in corners[0][0]]
# print(newCorners)
# newImg = gray[100:199,100:199]
# cv2.imshow('dfdfd',newImg)
# Print the detected markers
# print("Detected markers:", ids)
if ids is not None:
    cv2.aruco.drawDetectedMarkers(image, corners, ids)
    cv2.imwrite("marked.png",image)
    cv2.imshow('Detected Markers', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
