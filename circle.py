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
    for i in range(2):
        if(circlesCentres[2][0] - circlesCentres[i][0] == 0):
            angles.append(0)
        else:
            tmp = math.atan((circlesCentres[2][1] - circlesCentres[i][1]) / (circlesCentres[2][0] - circlesCentres[i][0]))
            angles.append(tmp)
    angles.sort()

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
    i = 0
    while (i != circlesCentres.__len__() - 2):
        if (i == 0):
            tmp = angles[1] - math.pi
        else:
            tmp = angles[1]
        angle = []
        if (i == 0):
            max_angle = angles[0]
        else:
            max_angle = angles[0] + math.pi
        while tmp < max_angle:
            angle.append(tmp)
            tmp += math.pi / 180
        angle.append(max_angle)

        for a in angle:
            if (a == angle[0]):
                r = circlesRadius[2]
                xPrev = circlesCentres[2 + i][0] + r * math.cos(a)
                yPrev = circlesCentres[2 + i][1] + r * math.sin(a)
            else:
                x = circlesCentres[2 + i][0] + r * math.cos(a)
                y = circlesCentres[2 + i][1] + r * math.sin(a)

                drawLine = plt.Line2D((xPrev, x),
                                      (yPrev, y),
                                      lw=0.5,
                                      markeredgecolor='r')
                plt.gca().add_line(drawLine)
                xPrev = x
                yPrev = y
        i += 1

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