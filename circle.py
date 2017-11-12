import matplotlib.pyplot as plt
import random as rnd
import math

inputFile = open("inputCircle.txt", "r")
outputFile = open("outputCircle.txt", "w")

circlesCentres = []
circlesRadius = []
arc = []

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
    circlesRadius.append(int(inputFile.readline()))

#FIXME r for arg is not exist
def generateCircles():
    for i in range(2):
        point = [rnd.randint(-10, 10),
                 rnd.randint(-10, 10)]
        r = rnd.randint(0, 10)
        circlesCentres.append(point)
        circlesRadius.append(r)
    circlesRadius.append(rnd.randint(0, 10))

def checkRadius():
    # if (circlesRadius[2] < circlesRadius[0] or circlesRadius[2] < circlesRadius[1]):
    #     return False
    dx = abs(circlesCentres[1][0] - circlesCentres[0][0])
    dy = abs(circlesCentres[1][1] - circlesCentres[0][1])
    d = (dx**2 + dy**2) ** 0.5
    # print d
    # if (d + circlesRadius[0] + circlesRadius[1] < 2* circlesRadius[2]):
    #     return False
    # if (d - circlesRadius[0] - circlesRadius[1] > 2* circlesRadius[2]):
    #     return False
    # if (min(circlesRadius[0], circlesRadius[1]) + d <= max(circlesRadius[0], circlesRadius[1])):
    #     return False
    # if (2*circlesRadius[2] < d):
    #     return False

    d1 = circlesRadius[0] + circlesRadius[2]
    d2 = circlesRadius[1] + circlesRadius[2]
    if (abs(d1 - d2) < d < d1 + d2):
        if (circlesCentres[0][0] < circlesCentres[1][0]):
            startPoint = circlesCentres[0]
            a = circlesRadius[2] - circlesRadius[0]
            b = circlesRadius[2] - circlesRadius[1]
        else:
            startPoint = circlesCentres[1]
            a = circlesRadius[2] - circlesRadius[1]
            b = circlesRadius[2] - circlesRadius[0]
        angle = (b**2 + d**2 - a**2)/(2*d*b)
        if (abs(angle) > 1):
            return False
        x = a * angle
        angle = (1 - angle**2)**0.5
        y = a * angle

        if (circlesCentres[1][0] - circlesCentres[0][0]) != 0:
            angle = (circlesCentres[1][1] - circlesCentres[0][1])/(circlesCentres[1][0] - circlesCentres[0][0])
            angle = math.atan(angle)
            x = x*math.cos(angle) + startPoint[0]
            y = y*math.sin(angle) + startPoint[1]
            circlesCentres.append([x,y])
        else:
            x = x + startPoint[0]
            y = y + startPoint[1]
            circlesCentres.append([x, y])
        return True
    elif(d1 + d2 == d):
        x = (circlesCentres[0][0] * d1 + circlesCentres[1][0] * d2) / d
        y = (circlesCentres[0][1] * d1 + circlesCentres[1][1] * d2) / d
        circlesCentres.append([x, y])
        return True
    else: #(d > d1 + d2 or d <= abs(d1 - d2)):
        return False

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
    circle.append(plt.Circle((circlesCentres[2][0],
                              circlesCentres[2][1]),
                             circlesRadius[2],
                             color='r',
                             fill=False))
    ax.add_patch(circle[2])

def drawingArc():
    return

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