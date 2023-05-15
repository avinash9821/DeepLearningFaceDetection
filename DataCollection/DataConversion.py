# This class is dedicated for data conversion from Images to csv values
import os

import cv2


# This function reads the gray values of image at imagePath return gray Values with image name
def convertDataFromImagesToCsv(imagePath):
    # Converting the JPG files to JPEG
    if imagePath.endswith(".jpg"):
        img = cv2.imread(imagePath)
        cv2.imwrite(imagePath[0:-4]+".jpeg", img)
        os.remove(imagePath)
        return cv2.imread(imagePath[0:-4]+".jpeg")
    else:
        return cv2.imread(imagePath)
