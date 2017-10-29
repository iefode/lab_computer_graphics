import matplotlib.pyplot as plt
import random as rnd

inputFile = open("input.txt", "r")
outputFile = open("output.txt", "w")

#global variable
polygon = []
line = []

#parse of string to list for point
def parseStringToPolygon():
    point = inputFile.readline()
    point = point.replace('(', '')
    point = point.replace(')', '')
    point = point.replace('\n', '')
    point = point.split(",")
    return [int(point[0]), int(point[1])]

#parser of input file
def parseInputFile():
    numberPoint = int(inputFile.readline())
    while (polygon.__len__() != numberPoint):
        polygon.append(parseStringToPoint())
    while (line.__len__() != 2):
        line.append(parseStringToPolygon())

#adding new point in polygon
def addPointInRolygon(points):
    newPoint = [rnd.randint(-10, 10),
                rnd.randint(-10, 10)]
    if (newPoint in polygon):
        return
    numberPoint = polygon.__len__()
    if (numberPoint < 3):
        polygon.append(newPoint)
    else:
        #check last point
        if (numberPoint == points-1):
            n = 2
        else:
            n = 1
        for i in range(n):
            while (line.__len__() != 0):
                line.pop()
            if (i == 1):
                #check line as newPoint and polygon[0]
                idx = 0
                tempPoint = polygon.pop(0)
            else:
                idx = numberPoint - 1
                tempPoint = polygon.pop(numberPoint - 1)
            line.append(newPoint)
            line.append(tempPoint)
            if not(checkLine(True)):
                    polygon.insert(idx, tempPoint)
                    if (i == n-1):
                        polygon.append(newPoint)
            else:
                polygon.insert(idx, tempPoint)
                return

# generate random polygon
def generatePolygon():
    numberPoint = rnd.randint(3, 10)
    while (polygon.__len__() != numberPoint):
        addPointInRolygon(numberPoint)

# generate random line
def generateLinePoints():
    while (line.__len__() != 0):
        line.pop()
    while(line.__len__() != 2):
        line.append([rnd.randint(-10, 10),
                       rnd.randint(-10, 10)])

def checkLine(flagCheckPoint):
    for currentPoint in polygon:
        indexCurrentPoint = polygon.index(currentPoint)
        if (flagCheckPoint and (indexCurrentPoint == polygon.__len__() - 1)):
            continue
        nextPoint = polygon[(indexCurrentPoint + 1) % polygon.__len__()]
        if (currentPoint in line or
            nextPoint in line):
            return True
        k1 = None
        k2 = None
        b1 = None
        b2 = None
        if ((currentPoint[0] - nextPoint[0]) != 0):
            k1 = float(nextPoint[1] - currentPoint[1])/(nextPoint[0] - currentPoint[0])
            b1 = float(-k1*currentPoint[0] + currentPoint[1])
        if ((line[1][0] - line[0][0]) != 0):
            k2 = float(line[1][1] - line[0][1]) / (line[1][0] - line[0][0])
            b2 = float(-k2*line[0][0] + line[0][1])

        maxLineY = max(line[0][1], line[1][1])
        minLineY = min(line[0][1], line[1][1])
        maxPolygonY = max(currentPoint[1], nextPoint[1])
        minPolygonY = min(currentPoint[1], nextPoint[1])
        if (k1 == k2) and (b1 == b2):
            if (k1 == None and currentPoint[0] != line[0][0]):
                continue
            if ((minLineY > maxPolygonY) or
                (maxLineY < minPolygonY)):
                continue
            else:
                return True
        elif (k2 == None):
            y = k1 * line[0][0] + b1
            if (minPolygonY <= y <= maxPolygonY):
                return True
            else:
                continue
        elif (k1 == None):
            y = k2 * currentPoint[0] + b2
            if (minLineY <= y <= maxLineY):
                return True
            else:
                continue
        elif (k1 == k2):
            continue
        x = (b2 - b1) / (k1 - k2)
        y = k1*x + b1
        if (minLineY <= y <= maxLineY and
            minPolygonY <= y <= maxPolygonY):
            return True
        else:
            continue
    return False

def drawingPolygon(n):
    i = 0
    for i in range(n):
        j = (i+1) % n
        drawPolygon = plt.Line2D((polygon[i][0], polygon[j][0]),
                                  (polygon[i][1], polygon[j][1]),
                                  lw=2.5)
        plt.gca().add_line(drawPolygon)

def drawingLine():
    #drawing line
    drawLine = plt.Line2D((line[1][0], line[0][0]),
                             (line[1][1], line[0][1]),
                             lw=2.5,
                             ls='-.',
                             marker='.',
                             markersize=50,
                             markerfacecolor='r',
                             markeredgecolor='r',
                             alpha=0.5)
    plt.gca().add_line(drawLine)

def printInfo():
    outputFile.write("Number of point: " + polygon.__len__().__str__())
    outputFile.write("\nCoordinates of points of poligon:\n" + polygon.__str__())
    outputFile.write("\nCoordinates of points of line:\n" + line.__str__())
    outputFile.write("\nLine and polygon: " + checkLine(False).__str__())

# parseInputFile()
generatePolygon()
generateLinePoints()
printInfo()
drawingLine()
drawingPolygon(polygon.__len__())
print checkLine(False)

plt.axes()
plt.axis('scaled')
plt.show()