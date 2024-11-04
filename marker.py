import cv2
import numpy as np
import matplotlib.pyplot as plt

aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)

marker_id = 50
marker_size = 100  
marker_image = cv2.aruco.generateImageMarker(aruco_dict, marker_id, marker_size)

cv2.imwrite('marker_'+str(marker_id)+'.png', marker_image)
# plt.imshow(marker_image, cmap='gray', interpolation='nearest')
# plt.axis('off')  # Hide axes
# plt.title(f'ArUco Marker {marker_id}')
# plt.show()
