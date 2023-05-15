import time
import logging

from DataBalancing import DataBalancingDetection, DataGenerator

logging.basicConfig(level=logging.INFO)


def balancedData(imageData, targetNames, path):
    logging.info("Checking for Data Balancing....")
    #time.sleep(2)
    if DataBalancingDetection.detectBalance(targetNames=targetNames):
        #time.sleep(1)
        logging.info("The Data is Balanced")
    else:
        #time.sleep(1)
        logging.info("The Data is Not Balanced....")
        #time.sleep(2)
        logging.info("The Data is going through Data Balancing process.....")
        #time.sleep(2)
        return DataGenerator.generateData(imageData, targetNames)
