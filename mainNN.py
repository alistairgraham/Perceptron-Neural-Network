# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 14:54:20 2019

@author: Alistair Graham
"""

import sys
import random

from image import Image
from image import Feature

#import Perceptron

def loadImages (filename):
    imageList = []
    file = open(filename, "r")
    
    #For each image in file
    while True:
        filetypeLine = file.readline()
        # Check if EOF
        if not filetypeLine:
            break
        
        # Get filetype
        filetype = filetypeLine.split()[0]
        if filetype != "P1":
            print("Not a P1 file: ", end = '')
            raise ValueError
        
        categoryLine = file.readline()
        
        # Get image output, black or white
        category = list(categoryLine)[1]
        if category == 'X':
            category = 1
        elif category == 'O':
            category = 0
        else:
            raise ValueError
        # Get row and col length of image
        rowCols = file.readline().split()
        numOfRows = rowCols[0]
        numOfCols = rowCols[1]
        
        # Create 2D array of bits
        imgData = []
        for row in range(0, int(numOfRows)):
            rowData = []
            for col in range(0, int(numOfCols)):
                char = file.read(1)
                while char == '\n':
                    char = file.read(1)
                rowData.append(char)
            imgData.append(rowData)
            
        imageList.append(Image(imgData, category))
        file.readline()
    file.close()
    return imageList

def constructRandomFeatures (rowLength, colLength, numOfFeatures):
    numOfPixels = 4
    featureList = []    
    
    for i in range(0, numOfFeatures):
        rows = []
        cols = []
        connections = []
        # Create random values for rows, cols of pixels
        # and random true or false values for connections to the four pixels
        for i in range(0, numOfPixels):
            rows.append(random.randint(0, rowLength-1))
            cols.append(random.randint(0, colLength-1))
            connections.append(random.randint(0,1))
        featureList.append(Feature(rows, cols, connections))
    
    return featureList

def createInputs (imageList, feature):
    imagesForInput = []
    imageInputs = []
    for image in imageList:
        
    return

"""def trainPerceptron (perceptron, imageInputsList):
    if not isinstance(perceptron, Perceptron):
        raise TypeError
        
    return"""




def main():
    imageList = loadImages(sys.argv[1])
    featureList = constructRandomFeatures(len(imageList[0].getData[0]), len(imageList[0].getData[0][0]), 50)
    imageInputsList = createInputs(imageList, featureList)
    #perceptron = Perceptron()
    #trainPerceptron(perceptron, imageInputsList)
    
    
main()

