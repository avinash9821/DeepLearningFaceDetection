import os
import time
import logging
import shutil


from BalancedDataCollection import DataCollection
from DataCollection import DriverClass, DataConversion
from tqdm import tqdm

logging.basicConfig(level=logging.INFO)


# This function will collect the track of the generated Images.
# Function collects the counts the generated Data to insert necessary original Images.
def trackGeneratedData(originalDataDic, generatedData):
    generatedDataDic = {"Counts": {}}
    for data in tqdm(generatedData, desc="TASK: Formatting the Generated Images in to dictionary "):
        if data[1] in generatedDataDic["Counts"]:
            generatedDataDic[data[1]].append(data[0])
            generatedDataDic["Counts"][data[1]] += 1
        else:
            generatedDataDic["Counts"][data[1]] = 1
            generatedDataDic[data[1]] = [data[0]]
    return DataCollection.collectData(originalDataDic, generatedDataDic)


def collectionDriver(originalDataDic, generatedPath):
    fetchedDataInfo = [(DataConversion.convertDataFromImagesToCsv(imagePath[0]), imagePath[1]) for imagePath in
                       tqdm(DriverClass.readingImagesPaths(generatedPath), desc="TASK: Reading the Generated Images "
                                                                                "in the generatedPath", unit="Images")]
    logging.info("Deleting the generated images which are already read....")
    time.sleep(4)
    for i in tqdm(os.listdir(generatedPath), desc="TASK: Deleting the generated Images after reading      ", unit="Images"):
        time.sleep(0.0005)
        shutil.rmtree(generatedPath + "/" + i)
    return trackGeneratedData(originalDataDic, fetchedDataInfo)
