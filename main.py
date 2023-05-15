from BalancedDataCollection import BalancedDataCollectionDriver
from DataBalancing import DataBalancingDriver
from DataCollection import DriverClass

import numpy as np

from DataProcessing import DataPreProcessingDriver
from DetectionModels import DetectionModelDriver, GRAPHS
from FinalDataFormating import FinalDataFormatingDriver

if __name__ == '__main__':
    path = "f22-dataset"
    # Collects the Images and performs reading the images along with target names
    (imageData, targetNames) = DriverClass.DriverFunction(path)
    # DataBalancing
    originalData = DataBalancingDriver.balancedData(imageData, targetNames, path)
    # Collect the Balanced Data
    finalData, finalTargets = BalancedDataCollectionDriver.collectionDriver(originalData, "GenerateData")
    # Get the final normalized data along with targets
    normalizedData, labelEncodedTargets = DataPreProcessingDriver.preProcessing(finalData, finalTargets)

    # Final step of Data Formatting
    finalFormattedData = FinalDataFormatingDriver.driver(normalizedData, (100, 100))

    # Model Creation, Training, Testing
    modelHistory = DetectionModelDriver.driver(finalFormattedData, labelEncodedTargets)

    # Plotting Graphs
    GRAPHS.plots(modelHistory)





