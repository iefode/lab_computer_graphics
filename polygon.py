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

#adding new point in polygon
def addPointInRolygon():
    newPoint = [rnd.randint(-10, 10),
                rnd.randint(-10, 10)]
    if (points.__len__() < 4):
        points.append(newPoint)
    else:
        line.append(newPoint)
        line.append(points[points.__len__() - 1])
        if (checkLine()):
            points.append(newPoint)
        while (line.__len__() != 0):
            line.pop()


# generate random polygon
def generatePolygon():
    numberPoint = rnd.randint(3, 10)
    # print numberPoint
    while (points.__len__() != numberPoint):
        addPointInRolygon()

# generate random line
def generateLinePoints():
    while(line.__len__() != 2):
        points.append([rnd.randint(-10, 10),
                       rnd.randint(-10, 10)])

def checkLine():
    for currentPoint in points:
        nextPoint = points.pop((points.index(currentPoint) + 1)) % points.__len__()
        print nextPoint
        if ((currentPoint[0] - nextPoint[0]) != 0):
            k1 = (nextPoint[1] - currentPoint[1])/(nextPoint[0] - currentPoint[0])
            b1 = k1*currentPoint[0] - currentPoint[1]
        if ((line[1][0] - line[0][0]) != 0):
            k2 = (line[1][1] - line[0][1]) / (line[1][0] - line[0][0])
            b2 = k2*line[0][0] - line[0][1]

        if (k1 == k2) and (b1 == b2):
            if (k1 == None and currentPoint[0] != line[0][0]):
                continue
            maxLineY = max(line[0][1], line[1][1])
            minLineY = min(line[0][1], line[1][1])
            maxPointsY = max(currentPoint[1], nextPoint[1])
            minPointsY = min(currentPoint[1], nextPoint[1])
            if ((minLineY > maxPointsY) or
                (maxLineY < minPointsY)):
                continue
            else:
                return True
        else:
            continue

        # test this
        y3 = k1 * line[0][0] + b1 - line[0][1]
        y4 = k2 * line[1][0] + b2 - line[1][1]
        print y3
        print y4

        if (y3 * y4 <= 0):
            return True
        else:
            continue
    return False

parseInputFile()
generatePolygon()