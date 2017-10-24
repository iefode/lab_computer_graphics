import matplotlib.pyplot as plt
import random as rnd

inputFile = open("input.txt", "r")
outputFile = open("output.txt", "w")

#global variable
points = []
line = []

#parse of string to list for point
def parseStringToPoint():
    point = inputFile.readline()
    point = point.replace('(', '')
    point = point.replace(')', '')
    point = point.replace('\n', '')
    point = point.split(",")
    return [int(point[0]), int(point[1])]

#parser of input file
def parseInputFile():
    numberPoint = int(inputFile.readline())
    while (points.__len__() != numberPoint):
        points.append(parseStringToPoint())
    while (line.__len__() != 2):
        line.append(parseStringToPoint())


parseInputFile()