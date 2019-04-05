# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 15:35:38 2019

@author: Alistair Graham
"""
import random

class Image:
    
    def __init__(self, imgData, category):
        self.imgData = imgData
        self.category = category
        self.featureList = []
    
    @property
    def getData(self):
        return self.imgData
    
    def addFeature(self, feature):
        self.featureList.append(feature)
        
    def getFeature(self, index):
        return self.featureList[index]
        
class Feature:
    
    def __init__(self, rowList, colList, connectionList):
        self.rowList = rowList
        self.colList = colList
        self.connectionList = connectionList
        
class Perceptron:
    
    def __init__(self, numOfFeatures):
        self.numOfFeatures = numOfFeatures
        self.weights = []
        
        #bias
        self.weights.append(1)
        for i in range(0, numOfFeatures):
            randomInt = random.randint(0,1)
            if (randomInt == 0):
                self.weights.append(float(-1))
            elif (randomInt == 1):
                self.weights.append(float(1))
            else:
                raise ValueError
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    