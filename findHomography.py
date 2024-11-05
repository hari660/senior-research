import cv2
import numpy as np

# Load the images
img1 = cv2.imread("reference.png")
img2 = cv2.imread("shifted.png")

if img1 is None or img2 is None:
    print("One or both images could not be loaded. Check the file paths.")
else:
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # Define the dictionary and parameters for ArUco detection
    aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
    parameters = cv2.aruco.DetectorParameters()
    parameters.adaptiveThreshConstant = 7  # Adjust as needed

    # Create the ArUco detector
    detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)

    # Detect the markers in both images
    corners1, ids1, _ = detector.detectMarkers(gray1)
    corners2, ids2, _ = detector.detectMarkers(gray2)
    if ids1 is not None and ids2 is not None:
        # Find common markers between the images
        common_ids = np.intersect1d(ids1.flatten(), ids2.flatten())
        # print(common_ids)
        if len(common_ids) >= 2:  # Ensure at least 2 common markers
            src_pts = []
            dst_pts = []
            
            for marker_id in common_ids:
                # Find the marker index in both images
                idx1 = np.where(ids1.flatten() == marker_id)[0][0]
                idx2 = np.where(ids2.flatten() == marker_id)[0][0]
                
                # Add marker corners to the points lists for homography calculation
                src_pts.extend(corners1[idx1][0])  # Points in image1
                dst_pts.extend(corners2[idx2][0])  # Points in image2

            # Convert points to numpy arrays
            src_pts = np.array(src_pts)
            dst_pts = np.array(dst_pts)
            
            # Compute the homography matrix
            H, _ = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC)
            
            print("Homography matrix:\n", H)
        else:
            print("Not enough common markers detected to compute homography.")
    else:
        print("Markers not detected in one or both images.")
