import matplotlib.pyplot as plt
import random as rnd
import math

inputFile = open("inputCircle.txt", "r")
outputFile = open("outputCircle.txt", "w")

circlesCentres = []
circlesRadius = []
arc = []
angles = []

def parseStringToPoint():
    point = inputFile.readline()
    point = point.replace('(', '')
    point = point.replace(')', '')
    point = point.replace('\n', '')
    point = point.split(",")
    return [int(point[0]), int(point[1])]

#parser of input file
def parseInputFile():
    while (circlesCentres.__len__() != 2 and
           circlesRadius.__len__() != 2):
        circlesCentres.append(parseStringToPoint())
        circlesRadius.append(int(inputFile.readline()))
    circlesRadius.append(float(inputFile.readline()))

#FIXME r for arg is not exist
def generateCircles():
    for i in range(2):
        point = [rnd.randint(-10, 10),
                 rnd.randint(-10, 10)]
        r = rnd.randint(0, 10)
        circlesCentres.append(point)
        circlesRadius.append(r)
    #radius for conjugation
    circlesRadius.append(rnd.randint(0, 10))

def checkRadius():
    dx = abs(circlesCentres[1][0] - circlesCentres[0][0])
    dy = abs(circlesCentres[1][1] - circlesCentres[0][1])
    d = (dx**2 + dy**2) ** 0.5
    d1 = circlesRadius[0] + circlesRadius[2]
    d2 = circlesRadius[1] + circlesRadius[2]
    if(d1 + d2 == d):
        x = (circlesCentres[0][0] * d1 + circlesCentres[1][0] * d2) / d
        y = (circlesCentres[0][1] * d1 + circlesCentres[1][1] * d2) / d
        circlesCentres.append([x, y])
        return True
    if (circlesRadius[0] + circlesRadius[1] == d):
        if (circlesCentres[0][0] < circlesCentres[1][0]):
            startPoint = circlesCentres[0]
            r = circlesRadius[0]
        else:
            startPoint = circlesCentres[1]
            r = circlesRadius[1]
        x = startPoint[0] + d - r
        y = 0
        circlesCentres.append([x,y])

        return True
    if (abs(d1 - d2) < d < d1 + d2):
        startPoint = circlesCentres[0]
        a = circlesRadius[2] - circlesRadius[1]
        b = circlesRadius[2] - circlesRadius[0]
        if (a + b <= d or
                        a + d <= b or
                        b + d <= a):
            return False
        if (circlesCentres[0][0] > circlesCentres[1][0]):
            startPoint = circlesCentres[1]
            tmp = a
            a = b
            b = tmp
        #cos of angle in triangle
        angle = (b**2 + d**2 - a**2)/(2*d*b)
        #projection of side triangle to d
        x = b * angle
        angle = (1 - angle**2)**0.5
        #high in triangle
        y = b * angle
        #converting relative coordinates (d) to absolute1
        if (circlesCentres[1][0] - circlesCentres[0][0]) != 0:
            k = float(circlesCentres[1][1] - circlesCentres[0][1])/(circlesCentres[1][0] - circlesCentres[0][0])
            b = startPoint[1] - angle * startPoint[0]
            angle = k
            angle = math.atan(angle)
            x = x*math.cos(angle) + startPoint[0]
        else:
            k = None
            b = None
            x += startPoint[0]
        if (circlesCentres[1][1] - circlesCentres[0][1]) != 0:
            tmp = k*x + b
            y1 = y*math.sin(angle) + tmp
            y2 = -y*math.sin(angle) + tmp
        else:
            tmp = startPoint[1]
            y1 = tmp + y
            y2 = tmp - y
        circlesCentres.append([x, y1])
        circlesCentres.append([x, y2])
        return True
    else:
        return False

def findAngles():
    j = 2
    while (j != circlesCentres.__len__()):
        angle = []
        for i in range(2):
            if(circlesCentres[2][0] - circlesCentres[i][0] == 0):
                angle.append(0)
            else:
                tmp = math.atan((circlesCentres[2][1] - circlesCentres[i][1]) / (circlesCentres[2][0] - circlesCentres[i][0]))
                if (i == 0):
                    tmp -= math.pi
                angle.append(tmp)
        angle.sort()
        angles.append(angle)
        j += 1

def drawingCircles():
    print circlesCentres
    print circlesRadius

    circle = []
    ax = plt.gca()
    ax.cla()
    for i in range(2):
        circle.append(plt.Circle((circlesCentres[i][0],
                                  circlesCentres[i][1]),
                                  circlesRadius[i],
                                  color='b',
                                  fill=False))
        ax.add_patch(circle[i])
    if (circlesCentres.__len__() == 3):
        circle.append(plt.Circle((circlesCentres[2][0],
                                  circlesCentres[2][1]),
                                 circlesRadius[2],
                                 color='r',
                                 fill=False))
        ax.add_patch(circle[2])
    else:
        drawingArc()

def drawingArc():
    findAngles()
    print angles
    angles[0][0] *= 180 / math.pi
    angles[0][1] *= 180 / math.pi
    print angles[0]
    tmp = angles[0][0]
    angle = []
    while tmp < angles[0][1]:
        angle.append(tmp)
        tmp += 1
    angle.append(angles[0][1])

    print angle

    r = circlesRadius[2]
    for a in angle:
        if (a == angle[0]):
            xPrev = circlesCentres[2][0] + r * math.cos(math.pi / 180 * a)
            yPrev = circlesCentres[2][1] + r * math.sin(math.pi / 180 * a)
        else:
            x = circlesCentres[2][0] + r * math.cos(math.pi / 180 * a)
            y = circlesCentres[2][1] + r * math.sin(math.pi / 180 * a)

            drawLine = plt.Line2D((xPrev, x),
                                  (yPrev, y),
                                  lw=0.5,
                                  markeredgecolor='r')
            plt.gca().add_line(drawLine)
            xPrev = x
            yPrev = y



    # for i in range(2):
    #     angle = []
        # range(angles[i][0], angles[i][1], 1)
        # grad = math.pi / 180
        # index = int((angles[i][1] - angles[i][0]) / grad)
        # for j in range(index-1):
        #     value = angles[i][0] + grad*j
        #     angle.append(value)
        # angle.append(angles[i][1])
        # xPrev = None
        # yPrev = None
        # for a in angle:
        #     if (xPrev == None):
        #         xPrev = circlesCentres[2 + i][0] + circlesRadius[2] * math.cos(a)
        #         yPrev = circlesCentres[2 + i][1] + circlesRadius[2] * math.sin(a)
        #         print xPrev
        #         print yPrev
        #         continue
        #     x = float(circlesCentres[2 + i][0] + circlesRadius[2] * math.cos(a))
        #     y = circlesCentres[2 + i][1] + circlesRadius[2] * math.sin(a)
        #     drawLine = plt.Line2D((xPrev, yPrev),
        #                           (x, y),
        #                           lw=2.5,
        #                           markeredgecolor='r')
        #     plt.gca().add_line(drawLine)
        #     xPrev = x
        #     yPrev = y

def printInfo():
    outputFile.write("Circles: " + circlesCentres.__str__() + ' ' + circlesRadius.__str__())

def output():
    # print circles
    printInfo()
    drawingCircles()
    plt.axes()
    plt.grid()
    plt.axis('scaled')
    plt.show()

mode = input("Enter a mode: 1 -manual, 2 - auto\n")
if (mode == 1):
    parseInputFile()
    if (checkRadius()):
        output()
    else:
        print "\nIs not possible for this case"
elif (mode == 2):
    generateCircles()
    print circlesCentres
    print circlesRadius
    if (checkRadius()):
        output()
    else:
        print "\nIs not possible for this case"
else:
    print "Uncorrect mode!"