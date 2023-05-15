import time
import cv2
import numpy as np

from tqdm import tqdm


def formatCollectedData(combinedDataDic):
    del combinedDataDic["Counts"]
    imageData = []
    targetName = []
    for personName in tqdm(combinedDataDic, desc="TASK: Formatting the Generated and Original Data       ", unit="Images"):
        for image in combinedDataDic[personName]:
            imageData.append(image)
            targetName.append(personName)
        time.sleep(0.02)
    return imageData, targetName


def collectData(originalDataDic, generatedDataDic):
    time.sleep(2)
    for personName in tqdm(originalDataDic, desc="TASK: Combining the Generated and Original Data        ", unit="Images"):
        if list == type(originalDataDic[personName]):
            try:
                for imageData in generatedDataDic[personName]:
                    originalDataDic[personName].append(imageData)
                originalDataDic["Counts"][personName] += generatedDataDic["Counts"][personName]
            except:
                pass
        else:
            continue
        time.sleep(0.01)
    return formatCollectedData(originalDataDic)
