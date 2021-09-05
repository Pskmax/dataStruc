# tuple
import math
a = "apple",1
print(a)
print(a[0])
print(a[1])

b = (True,6.5,"hello")
print(b[0])
print(b[1])
print(b[2])
print()

def distance(x1,y1,x2,y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def distance2(pointA,pointB):
    return math.sqrt((pointA[0] - pointB[0]) ** 2 + (pointA[1] - pointB[1]) ** 2)

d = distance(2,5,5,9)
print("output from distance:",d)

pointA = (2,5)
pointB = 5,9
d2 = distance2(pointA,pointB)
print("output from distance2:",d2)