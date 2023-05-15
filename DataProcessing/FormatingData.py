import numpy as np


# This function converts the color values to gray values.
# The main thing to implement this way is to reduce the computation time with cv2.cvtcolor()
def convertToGrayValues(data):
    red, green, blue = data[:, :, 0], data[:, :, 1], data[:, :, 2]
    return (0.2989 * red + 0.5870 * green + 0.1140 * blue).flatten()


def formatData(finalData, finalTargets):
    images, targetName = [], []
    for imagedata, target in zip(finalData, finalTargets):
        if type(np.array([])) == type(imagedata):
            images.append(imagedata)
            targetName.append(target)
    return np.array([convertToGrayValues(image) for image in images]), np.array(targetName)
