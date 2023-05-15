import numpy as np
from sklearn import preprocessing

from DataProcessing import FormatingData


def normalizeData(finalData):
    return finalData / 255.0


def encode():
    return preprocessing.LabelEncoder()


def labelEncoder(finalTargets):
    return encode().fit_transform(finalTargets)


def preProcessing(finalData, finalTargets):
    data, target = FormatingData.formatData(finalData, finalTargets)
    return normalizeData(data), labelEncoder(target)
