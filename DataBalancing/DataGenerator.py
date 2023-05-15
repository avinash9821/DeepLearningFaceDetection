import time

from DataBalancing import ShrinkImageVolumes, ImageGenerator
from tqdm import tqdm


def callGenerator(trackedData):
    for targetName in tqdm(trackedData.keys(), desc="TASK: Generating the volume of each Target to 200      ", unit="Images"):
        if list == type(trackedData[targetName]):
            ImageGenerator.imageGenerator(trackedData[targetName][0], 200, targetName)
        else:
            continue
        time.sleep(0.01)
    return trackedData


def shrinkData(imageData, targetNames):
    return ShrinkImageVolumes.shrinkImages(imageData, targetNames)


def generateData(imageData, targetNames):
    return callGenerator(shrinkData(imageData, targetNames))
