# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 15:35:38 2019

@author: Alistair Graham
"""

class Image:
    
    def __init__(self, imgData, category):
        self.imgData = imgData
        self.category = category
    
    @property
    def getData(self):
        return self.imgData
        
class Feature:
    
    def __init__(self, rowList, colList, connectionList):
        self.rowList = rowList
        self.colList = colList
        self.connectionList = connectionList