import numpy as np


def stackingData(imageData):
    return np.stack(imageData, axis=0).astype("float32")


def convertSize(imageData, shape):
    tempData = []
    for i in range(0, len(imageData)):
        tempData.append(imageData[i].reshape(shape).astype('float32'))
    return tempData


def driver(imageData, shape):
    return stackingData(convertSize(imageData, shape))
