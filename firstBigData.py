# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 10:51:06 2020

@author: mry10
"""


import csv

possibleFactors = [] #all the keys for the data set
possibleValues = {} # all the values for each key

def getNumOfFactors() -> int:
    num = 0
    
    num = int(input("How many factors do you want to account for(max of " +
                    str(len(possibleFactors)) + ")? "))
    while num < 1 or num > len(possibleFactors):
        num = int(input("Error, must be an int between 1 and "
                        + str(len(possibleFactors)) + ": "))
    return num

def getNumOfValues(currentFactor) -> int:
    num = int(input("How many values are you checking for?"))
    
    if len(possibleValues[currentFactor]) < 400:
        while num < 1 or num > len(possibleValues[currentFactor]):
            num = int(input("Error, must be an int between 1 and "
                        + str(len(possibleValues[currentFactor])) + ": "))
    return num

def getListOfValues(numOfValues, currentFactor) -> list:
    valueList = []
    
    i = 0
    while i < numOfValues:
        print("Possible options: ")
        print(possibleValues[currentFactor])
        value = input("Enter the value you want to look for: ")
        if len(possibleValues[currentFactor]) < 400:
            while not(value in possibleValues[currentFactor]):
                value = input("Error, not a possible value. Please re-enter: ")
        valueList.append(value)
        i += 1
    
    return valueList
    
def getListOfFactors(numOfDataTypes) -> list:
    factorList = []
    i = 0
    while i < numOfDataTypes:
        factor = input("Enter what factor you're checking: ")
        while (not factor in possibleFactors):
            factor = input("Error, not a possible factor. Please re-enter: ")
        factorList.append(factor)
        i += 1
    return factorList

def findNumCases(factorValueDict, factorList) -> list:
    numOfCases = []
    i = 0
    while i < len(factorList):
        num = 0
        for y in cases:
            if containsAllCurrentFactors(y, factorList, factorValueDict, i):#y[factorList[i]] in factorValueDict[factorList[i]]:
                num += 1
        numOfCases.append(int(num))
        i += 1
    return numOfCases

def printPercents(numOfCases, factorValueDict, factorList):
    print("The percentage of total cases where the " + factorList[0] + " is") 
    print(factorValueDict[factorList[0]])
    print("is " + str((numOfCases[0] / len(cases)) *100) + "%")
    i = 1
    while i < len(factorList): 
        print("The percentage of those cases where the " 
              + factorList[i] + " is") 
        print(factorValueDict[factorList[i]])
        
        print("is " + str((numOfCases[i] / numOfCases[i - 1]) *100) + "%")
        
        i += 1
def containsAllCurrentFactors(y, factorList, factorValueDict, i) -> bool:
    
    containsFactors = True
    c = 0
    while c <= i:
        if not(y[factorList[c]] in factorValueDict[factorList[c]]):
            containsFactors = False
        
        c += 1
    
    return containsFactors
fileName = input("Enter File Name: ")
dataFile = open(fileName + ".csv", newline = '')
dataReader = csv.DictReader(dataFile)

#set up lists
cases = [] #list of each dictionary

#get all the dictionaries to fill the lists

for currDict in dataReader: 
    cases.append(currDict)
    
for x in cases[1]:
    possibleFactors.append(x)

for x in possibleFactors:
    uniqueValues = []
    for y in cases:
        if not(y[x] in uniqueValues):
            uniqueValues.append(y[x])
        if len(uniqueValues) > 500:
            break
    possibleValues[x] = uniqueValues

willRun = "y"
while willRun == "y":
    #a dictionary that tracks the values the user wants to check per factor
    factorValueDict = {}
    
    numOfFactors = getNumOfFactors()
    factorList = getListOfFactors(numOfFactors) #list of factors the user wants to consider
    for x in factorList:
        num = getNumOfValues(x)
        valueList = getListOfValues(num, x)#values the user wants to check for the current factor
        factorValueDict[x] = valueList
        
    numOfCases = findNumCases(factorValueDict, factorList)
    
    printPercents(numOfCases, factorValueDict, factorList)
    willRun = input("Do you want to check more statistics? ")


