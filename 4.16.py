from vector_drawing import *
from vectors import add
import numpy as np 
from vectors import scale, add, to_polar, to_cartesian


def mirrorVec(vec):
    return((vec[0], -vec[1]))

vecs = []
arrows = []

v1 = (1, 5)

# v2 = scale(3, v1)
v2 = (4, 1)
v3 = add(v1, v2)

vecs.append(v1)
vecs.append(v2)
# vecs.append(v3)
v3 = add(mirrorVec(v1), mirrorVec(v2))
vecs.append(v3)


for vec in vecs:
    arrows.append(Arrow(vec, color=blue))

# for vec in vecs:
#     arrows.append(Arrow(mirrorVec(vec), color=red))

draw(*arrows)
