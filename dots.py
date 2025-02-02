from vector_drawing import *
from add import add
import numpy as np 


u=(-1,1)
v=(1,1)

rar = np.arange(-3,3,0.3)
sar = np.arange(-1,1,0.3)

points = []

for r in rar:
    for s in sar:
        points.append(add(((u[0]*r, u[1]*r), (v[0]*s, v[1]*s))))
print(points)
draw(Points(*points))
