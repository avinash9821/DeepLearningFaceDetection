from DataCollection.DataConversion import convertDataFromImagesToCsv
from DataCollection.ReadData import readDirectorypath, readDirectory

from tqdm import tqdm
from time import sleep


def readingImagesPaths(directoryPath):
    return [(directoryPath + "/" + imageFolder + "/" + imageName, imageFolder)
            for imageFolder in
            tqdm(readDirectory(directoryPath), desc="TASK: Reading the Images in the directoryPath          ", unit="Images")
            for imageName in readDirectorypath(directoryPath + "/" + imageFolder)]


def DriverFunction(path):
    fetchedData = [(convertDataFromImagesToCsv(imagePath[0]), imagePath[1]) for imagePath in readingImagesPaths(path)]
    imageData, targetNames = [], []
    for data in tqdm(fetchedData, desc="TASK: Separating Image Data and Target Names           ", unit="Images"):
        imageData.append(data[0])
        targetNames.append(data[1])
        sleep(0.01)
    return imageData, targetNames
