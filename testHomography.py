import cv2
import numpy as np

img1 = cv2.imread("reference.png")
img2 = cv2.imread("shifted.png")
H = np.array([[ 1.00000000e+00, -5.59912153e-16,  2.50000000e+01],
 [ 3.10698123e-16,  1.00000000e+00,  2.50000000e+01],
 [ 1.18731603e-18, -1.55922808e-18,  1.00000000e+00]])
# Assume H is your computed homography matrix
height, width = img1.shape[:2]

# Warp img2 to the perspective of img1
try:
    warped_img2 = cv2.warpPerspective(img2, H, (width*2, height*2))
except Exception as e:
    print("Error during warping:", e)
# Display the result
cv2.imshow("Warped Image", warped_img2)
cv2.imwrite("TestingWarped.png",warped_img2)
cv2.imshow("Reference Image", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
