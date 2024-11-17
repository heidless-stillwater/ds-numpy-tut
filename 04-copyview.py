import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle

from icecream import ic

# configure logging
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(
    filename='./logs/04-copyview.log',
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')
    
def intro():
    logger.info(f"in {intro.__name__}")

    list1 = [1,2,3,4,5]
    # ic(list1)
    # logger.info(f"{ic(list1)}")
    
    list2 = ["heidless", 42, list1, True]
    
    # Numpy = Numeric Python
    
    np1 = np.array([0,1,2,3,4,5,6,7,8,9])
    logger.info(f"np1: {np1}")

    # shape
    np1.shape
    logger.info(f"np1: {np1.shape}")

    # range
    np2 = np.arange(10)
    logger.info(f"np2: {np2}")

    # step
    np3 = np.arange(0,10,2)
    logger.info(f"np3: {np3}")
    
    # zeros
    np4 = np.zeros(10)
    logger.info(f"np4: {np4}")
    
    # multi-dimensional zeros
    np5 = np.zeros((2,10))
    logger.info(f"np5: {np5}") 
    
    # full
    np6 = np.full((10), 6)
    logger.info(f"np6: {np6}") 
    
    # multi-dimensional full
    np7 = np.full((2,10), 5)
    logger.info(f"np7: {np7}") 
    
    # convert python lists to np
    my_list = [1,2,3,4,5]
    np8 = np.array(my_list)
    logger.info(f"np8: {np8}")
     
    logger.info(f"np8: {np8[0]}")

def slice():
    logger.info(f"in {slice.__name__}")
    
    np1 = np.array([1,2,3,4,5,6,7,8,9])
    
    # slicing numpy arrays
    slice1 = np1[1:5]
    logger.info(f"slice1: {slice1}")

    # return from something till the end
    slice2 = np1[3:]
    logger.info(f"slice2: {slice2}")

    # -ve slices
    # 7, 8
    slice3 = np1[-3:-1]
    logger.info(f"slice3: {slice3}")

    # steps
    slice4 = np1[1:5]   # 2 - 5
    logger.info(f"slice4: {slice4}")
    slice5 = np1[1:5:2]
    logger.info(f"slice5: {slice5}")

    # steps of entire array
    steps1 = np1[::3]  
    logger.info(f"steps1: {steps1}")
    
    # slice a 2-d arrary
    np2 = np.array([
                    [1,2,3,4,5], 
                    [6,7,8,9,10]
                ])
    
    logger.info(f"slice6: {np2}")  
    
    # pull out single item
    val1 = np2[1,2]
    logger.info(f"val1: {val1}")  

    # slice a 2-d array
    slice5 = np2[0:1,1:3]
    logger.info(f"slice5: {slice5}")  

    # slice from both rows
    slice6 = np2[0:2,1:3]
    logger.info(f"slice6: {slice6}")  

def fun():
    logger.info(f"in {fun.__name__}")
    
    np1 = np.array([-3,-2,-1,0,1,2,3,4,5,6,7,8,9])
    logger.info(f"{np1}")

    # square root
    # func1 = np.sqrt(np1)
    
    # absolute value
    # func1 = np.absolute(np1)
    
    # exponential
    # func1 = np.exp(np1)
    
    # min/max
    func1 = np.min(np1)
    
    # sign
    func1 = np.sign(np1)
    
    # trig / sin / cos / log
    func1 = np.sin(np1)
    
    
    logger.info(f"func1: {func1}")

def copyview():
    logger.info(f"in {copyview.__name__}")
    
    np1 = np.array([0,1,2,3,4,5])

    # create a view
    # np2 = np1.view()
  
    # logger.info(f"original np1: {np1}")
    # logger.info(f"original np2: {np2}")
  
    # np1[0] = 41
    
    # logger.info(f"updated np1: {np1}")
    # logger.info(f"updated np2: {np2}")
  
    # create a copy
    np2 = np1.copy()
    
    logger.info(f"original np1: {np1}")
    logger.info(f"original np2: {np2}")

    np2[0] = 42

    logger.info(f"updated np1: {np1}")
    logger.info(f"updated np2: {np2}")




    
def main():
    logger.info('--------') 
    # loggers.info('Calling nump tutorials')
    copyview()
    
if __name__ == '__main__':
    main()

