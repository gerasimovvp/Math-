import numpy as np
from vector_drawing import *

dino_vectors = [(6,4),(3,1),(1,2),(-1,5),(-2,5),(-3,4),(-4,4),(-5,3),(-5,2),(-2,2),(-5,1),(-4,0),(-2,1),(-1,0),(0,-3),(-1,-4),(1,-4),(2,-3),(1,-2),(3,-1),(5,1)]

def subtract(v1, v2):
    return (v1[0] - v2[0], v1[1] - v2[1])

def length(v):
    return(np.sqrt(v[0]**2 + v[1]**2))

#print(length((3,4)))

def distance(v1, v2):
    return length(subtract(v1, v2))

#print(distance((1,2), (-3,8)))

def perimeter(vecs):
    sum = 0
    for i in range(len(vecs)-1):
        sum += distance(vecs[i], vecs[i+1])
    sum += distance(vecs[len(vecs)-1], vecs[0])
    return sum

#print(length((-1.34, 2.68)))
#print(np.atan(37))

#print(np.tan(116.57 / 57))

#print(10 * np.pi/6 * 57)
#print("cos: %f  sin: %f" %  (np.cos(10*np.pi/6), np.sin(10*np.pi/6)))

a = [(np.cos(5*x*np.pi/500.0), 2*np.pi*x/1000.0) for x in range(0, 1000)]
#print(a)

#decList = []
#for vec in a:
#    decList.append((vec[0]*np.cos(vec[1]), vec[0]*np.sin(vec[1])))
#for i in decList:
#    print(i)
#draw(Polygon(*decList))

#angle = np.pi/2
#while np.sin(angle) > (3 / np.sqrt(13)):
#    print(angle)
#    angle += 0.0001
#print("angle: %d" % angle)
#angle = angle * 57    
#print("angle: %d" % angle)

#print("ANGLE: %f" % np.atan(-3/2))

def convert_to_vec(point1, point2):
    return((point2[0]-point1[0], point2[1]-point1[1]))

def angle(vec1, vec0):
    return (np.arctan2(vec1[1], vec1[0]) - np.arctan2(vec0[1], vec0[0]))

def toAngular(vec):
    return((np.sqrt(vec[0]**2 + vec[1]**2), np.arctan2(vec[1] , vec[0])))

def toCartesian(vec):
    return((vec[0]*np.cos(vec[1]), vec[0]*np.sin(vec[1])))

#print(angle(convert_to_vec((-5,2),(-2,2)), convert_to_vec((-1.9,-5), (-2,2)))*57)
def rotate(angle, vectors):
    vecs_rot = []
    for vector in vectors:
        vecs_rot.append(toCartesian((toAngular(vector)[0], toAngular(vector)[1] + angle)))
    return vecs_rot
#draw(Polygon(*dino_vectors), Polygon(*rotate(np.pi/6, dino_vectors), color = red))

def regular_polygon(n):
    vecs = []
    angle = 2*np.pi/n
    for i in range(n):
        vecs.append(toCartesian((1, angle*i)))
    draw(Polygon(*vecs))

regular_polygon(6)
