import matplotlib.pyplot as plt
import random as rnd

inputFile = open("inputCircle.txt", "r")
outputFile = open("outputCircle.txt", "w")

circles = []
duge = []

def parseStringToPoint():
    point = inputFile.readline()
    point = point.replace('(', '')
    point = point.replace(')', '')
    point = point.replace('\n', '')
    point = point.split(",")
    return [int(point[0]), int(point[1])]

#parser of input file
def parseInputFile():
    while (circles.__len__() != 2):
        circle = []
        circle.append(parseStringToPoint())
        circle.append(int(inputFile.readline()))
        circles.append(circle)
    duge.append(int(inputFile.readline()))

def generateCircles():
    for i in range(2):
        point = [rnd.randint(-10, 10),
                 rnd.randint(-10, 10)]
        r = rnd.randint(0, 10)
        circles.append([point, r])

def checkRadius():
    dx = abs(circles[0][0][0] - circles[1][0][0])
    dy = abs(circles[0][0][1] - circles[1][0][1])
    if (dx == 0 and dy == 0):
        return False
    minR = min(circles[0][1], circles[1][1])
    maxR = min(circles[0][1], circles[1][1])
    if (dx + minR <= maxR and
        dy + minR <= maxR):
        return False

    return True

def drawingCircles():
    print circles
    circle = []

    ax = plt.gca()
    ax.cla()
    for i in range(2):
        circle.append(plt.Circle((circles[i][0][0],
                                  circles[i][0][1]),
                                 circles[i][1],
                                 color='b',
                                 fill=False))
        ax.add_patch(circle[i])

def printInfo():
    outputFile.write("Circles: " + circles.__str__())

def output():
    print circles
    printInfo()
    drawingCircles()
    plt.axes()
    plt.grid()
    plt.axis('scaled')
    plt.show()

mode = input("Enter a mode: 1 -manual, 2 - auto\n")
if (mode == 1):
    parseInputFile()
    output()
elif (mode == 2):
    generateCircles()
    output()
else:
    print "Uncorrect mode!"