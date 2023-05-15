import time

from tqdm import tqdm


def shrinkImages(imageData, targetNames):
    trackTargets = {"Counts": {}}
    for index in tqdm(range(min(len(imageData), len(targetNames))), desc="TASK: Shrinking the volume of each Target to 50        ", unit="Images"):
        if targetNames[index] in trackTargets["Counts"] and trackTargets["Counts"][targetNames[index]] < 50:
            trackTargets[targetNames[index]].append(imageData[index])
            trackTargets["Counts"][targetNames[index]] += 1
        else:
            trackTargets["Counts"][targetNames[index]] = 1
            trackTargets[targetNames[index]] = [imageData[index]]

        time.sleep(0.01)
    return trackTargets
