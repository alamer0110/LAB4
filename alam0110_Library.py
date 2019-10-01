import math

def calculateMPG(galoonUsed,milesDriven):

    MPG = float(galoonUsed / milesDriven)
    return MPG


def calculateAreaofCirlce():
    radius = int(input("please enter a radius: "))
    areaofcircle = int(math.pi*radius ^ 2)


def convertFarenheighttoCelsius():
    temp = float(input("please enter a fahrenheit"))
    con = float((temp - 32) * (5 / 9))
    print(float(con))

def calculateDistanceBetweenPoints(x,x1,y,y1):

    a = x1 - x
    b = y1 - y
    print(a,b)

calculateDistanceBetweenPoints(1,5,3,7)

