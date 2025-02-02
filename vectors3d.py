import numpy as np
from draw3d import *
from math import sin, cos, acos, pi

#draw3d(
#        Points3D((2,2,2),(1,-2,-2)),
#        Arrow3D((2,2,2)),
#        Arrow3D((1,-2,-2)),
#        Box3D(2,2,2),
#        Box3D(1,-2,-2),
       
#        Points3D((2,2,2),(1,-2,-2))
#        )

#draw3d(Points3D((1,1,1), (1,1,-1), (1,-1,1), (-1,1,1), (-1,-1,-1), (-1,1,-1), (1,-1,-1) ,(-1,-1,1)), Segment3D((1,1,1), (1,1,-1)), Segment3D((1,-1,1),(1,-1,-1)), Segment3D((-1,-1,1),(-1,-1,-1)), Segment3D((-1,1,1),(-1,1,-1)), Segment3D((1,1,1),(1,-1,1)), Segment3D((1,-1,1),(-1,-1,1)), Segment3D((-1,-1,1),(-1,1,1)), Segment3D((-1,1,1),(1,1,1)), Segment3D((1,1,-1),(1,-1,-1)), Segment3D((1,-1,-1),(-1,-1,-1)), Segment3D((-1,-1,-1),(-1,1,-1)), Segment3D((-1,1,-1),(1,1,-1)))


vec1 = (4,0,3)
vec2 = (-1,0,1)
#print(vec1+vec2)
def sum(vec1, vec2):
    return(vec1[0] + vec2[0], vec1[1] + vec2[1], vec1[2] + vec2[2])

def draw2vecs(vec1, vec2):
    draw3d(Arrow3D(vec1), Arrow3D(sum(vec1, vec2), vec1), Arrow3D(vec2), Arrow3D(sum(vec2, vec1), vec2))

#draw2vecs(vec2, vec1)
arrowsList = []
vs = [(sin(pi*t/6), cos(pi*t/6), 1.0/3) for t in range(0,24)]
_sum = (0,0,0)
for vec in vs:
    arrowsList.append(Arrow3D(sum(_sum, vec), _sum))
    _sum = sum(_sum, vec) 

#draw3d(*arrowsList)
#print(_sum)

def subtract(v1, v2):
    return (coord[0] - coord[1] for coord in zip(v1, v2))


def scale(scalar, vector):
    return(tuple(dim * scalar for dim in vector))

#print(scale(5, (1,2,3)))

u = (1,-1,-1)
v = (0,0,2)

# find u+1/2(v-u)

#print(sum(u, scale(0.5, (sum(v, scale(-1, u))))))

def length(vector):
    _sum = 0
    return np.sqrt(np.sum(num**2 for num in vector))

#print(len((1,1,1,1)))

for i in range(20):
    for j in range(20):
        for k in range(20):
            if(length((i,j,k)) % 1 == 0):
                #print(i, j, k)
                pass


vec = (-1,-1,2)
divider = length(vec)


#print(len(scale(1/divider, (-1,-1,2))))


def dot(vec1, vec2):
    return np.sum([coord[0] * coord[1] for coord in zip(vec1, vec2)])

def angle(vec1, vec2):
    return acos(dot(vec1, vec2)/(length(vec1)*length(vec2)))

print(dot((-1,-1,1), (1,2,1)))
print(angle((-1,-1,1), (1,2,1))*180/pi)
print(acos(-1)*180/pi)

#range_i = np.arange(0, 10, 0.01)
#range_j = np.arange(0, 10, 0.01)
#for i in range_i:
#    print("i: ", i)
#for i in range_i:
#    for j in range_j:
#        #print(len((i,j)))
#        if(len((i, j)) == 3.0 or len((i,j)) == 7.0):
#            print("vec: (", i, " ", j, ")" )


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

#vec1 = (0,3)
#vec2 = (0,7)
#vecs_rot = []
#for angle in range(0, 180):
#    vec1 = toCartesian((toAngular(vec1)[0], toAngular(vec1)[1] + angle))
#    vec2 = toCartesian((toAngular(vec2)[0], toAngular(vec2)[1] + angle))
#    print("vec1: ", vec1)
#    print("vec2: ", vec2, "DOT: ", dot(vec1, vec2))



#print(3.61 * 1.44 * cos(101.3 * pi/180))

vec1 = (3,4)
vec2 = (4,3)

#print(angle(vec1, vec2))
#print(toAngular(vec1)[1] - toAngular(vec2)[1])

vec1 = (1,1,1)
vec2 = (-1,-1,1)

#print(angle(vec1, vec2) * 180/pi)

def cross(u, v):
    ux, uy, uz = u
    vx, vy, vz = v
    return(uy*vz - uz*vy, uz*vx - ux*vz, ux*vy - uy*vx)

def unit(v):
    return scale(1./length(v), v)

print(cross((0,0,1), (3,1,2)))


ribs = [
        [(0,0,1),(1,0,0)],
        [(0,0,1),(0,1,0)],
        [(0,0,1),(-1,0,0)],
        [(0,0,1),(0,-1,0)],
        [(0,0,-1),(1,0,0)],
        [(0,0,-1),(0,1,0)],
        [(0,0,-1),(-1,0,0)],
        [(0,0,-1),(0,-1,0)],
        [(1,0,0),(0,1,0)],
        [(0,1,0),(-1,0,0)],
        [(-1,0,0),(0,-1,0)],
        [(0,-1,0),(1,0,0)]
    ]


arrowsList = []

for rib in ribs:
    arrowsList.append(Segment3D(rib[0], rib[1]))
#draw3d(*arrowsList)
