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
        # print "points"
        # print points
        # print "new point"
        # print newPoint
        line.append(newPoint)
        line.append(points[points.__len__() - 1])
        # print "line"
        # print line
        if not (checkLine()):
            points.append(newPoint)
        while (line.__len__() != 0):
            line.pop()
        # print "line"
        # print line


# generate random polygon
def generatePolygon():
    numberPoint = rnd.randint(3, 5)
    print numberPoint
    # print numberPoint
    while (points.__len__() != numberPoint):
        addPointInRolygon()
    print points

# generate random line
def generateLinePoints():
    while(line.__len__() != 2):
        line.append([rnd.randint(-10, 10),
                       rnd.randint(-10, 10)])
    # print line

def checkLine():
    for currentPoint in points:
        nextPoint = points[(points.index(currentPoint) + 1) % points.__len__()]
        # print "iteration"
        # print currentPoint
        # print nextPoint
        # print line[0]
        # print line[1]
        if (currentPoint in line or
            nextPoint in line):
            return True
        # print nextPoint
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
        maxPointsY = max(currentPoint[1], nextPoint[1])
        minPointsY = min(currentPoint[1], nextPoint[1])
        # print "k1"
        # print k1
        # print "b1"
        # print b1
        # print "k2"
        # print k2
        # print "b2"
        # print b2
        if (k1 == k2) and (b1 == b2):
            if (k1 == None and currentPoint[0] != line[0][0]):
                continue
            if ((minLineY > maxPointsY) or
                (maxLineY < minPointsY)):
                continue
            else:
                return True
        elif (k2 == None):
            y = k1 * line[0][0] + b1
            if (minPointsY <= y <= maxPointsY):
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

        # test this
        x = (b2 - b1) / (k1 - k2)
        # print x
        y = k1*x + b1
        # print y
        #FIX ME
        if (minLineY <= y <= maxLineY and
            minPointsY <= y <= maxPointsY):
            return True
        else:
            continue
    return False

def drawingPolygon(n):
    # # drawing line for connection of first and last points
    # draw_polygon = plt.Line2D((points[n - 1][0], points[0][0]),
    #                           (points[n - 1][1], points[0][1]),
    #                           lw = 2.5)
    # plt.gca().add_line(draw_polygon)
    # drawing polygon
    i = 0
    for i in range(n):
        j = (i+1) % n
        draw_polygon = plt.Line2D((points[i][0], points[j][0]),
                                  (points[i][1], points[j][1]),
                                  lw=2.5)
        plt.gca().add_line(draw_polygon)

def drawingLine():
    #drawing line
    draw_line = plt.Line2D((line[1][0], line[0][0]),
                             (line[1][1], line[0][1]),
                             lw=2.5,
                             ls='-.',
                             marker='.',
                             markersize=50,
                             markerfacecolor='r',
                             markeredgecolor='r',
                             alpha=0.5)
    plt.gca().add_line(draw_line)

def printInfo():
    outputFile.write("Number of point: " + points.__len__().__str__())
    outputFile.write("\nCoordinates of points of poligon:\n" + points.__str__())
    outputFile.write("\nCoordinates of points of line:\n" + line.__str__())
    # outputFile.write("\nLine and polygon: " + checkLine().__str__())
    # print "\nLine and polygon: " + checkLine().__str__()

# parseInputFile()
generatePolygon()
generateLinePoints()

# printInfo()

#drawing of objects
drawingLine()
# print points.__len__()
# print points

drawingPolygon(points.__len__())
print checkLine()

plt.axes()
plt.axis('scaled')
plt.show()