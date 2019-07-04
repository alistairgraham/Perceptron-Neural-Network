# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 14:54:20 2019

@author: Alistair Graham
"""

import sys
import random

from perceptron import Image
from perceptron import Feature
from perceptron import Perceptron

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


def constructRandomFeatures (rowLength, colLength, numOfFeatures, numOfPixels):
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


def createInputs (imageList, featureList, numOfPixels):
    for image in imageList:
        # Biass
        image.addFeature(1)
        
        for f in featureList:
            sum = 0
            for i in range(0, numOfPixels):
                if (int(image.getData[f.rowList[i]][f.colList[i]]) == int(f.connectionList[i])):
                    sum += 1
            if (sum >= 3):
                image.addFeature(1)
            else:
                image.addFeature(0)
        

def trainPerceptron (perceptron, imageList, maxRepitions, trainingDelta):
    cycleCount = 0
    correctCount = 0
    
    while (correctCount < len(imageList) and cycleCount < maxRepitions):
        correctCount = 0
        for image in imageList:
            y = predict(perceptron, image.featureList)
            d = image.category
            
            if (y == d):
                correctCount += 1
            else:
                for i in range(1, len(perceptron.weights)):
                    perceptron.weights[i] += trainingDelta * (d - y) * image.featureList[i]  
        cycleCount += 1
    print("\nAccuracy = " + str((correctCount/len(imageList))*100) + "%")
    

def predict(perceptron, featureList):
    sum = 0
    count = 0
    # Get some of weights * features
    for i in range(0, len(featureList)):
        sum += perceptron.weights[count] * featureList[count]
        count += 1
    
    if (sum > 1):
        return 1
    else:
        return 0


def main():
    imageList = loadImages(sys.argv[1])
    numOfFeatures = 50
    numOfPixels = 4
    numOfRows = len(imageList[0].getData[0])
    numOfCols = len(imageList[0].getData[0][0])
    featureList = constructRandomFeatures(numOfRows, numOfCols, numOfFeatures, numOfPixels)
    
    createInputs(imageList, featureList, numOfPixels)
    perceptron = Perceptron(numOfFeatures)
    k = 150
    trainingDelta = 0.1
    trainPerceptron(perceptron, imageList, k, trainingDelta)
    
main()




