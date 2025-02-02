from vector_drawing import *
from add import add
import numpy as np 


u=(-1,1)
v=(1,1)

rar = np.arange(0, 6)
sar = np.arange(0, 6)

points = []

for r in rar:
    for s in sar:
        points.append((r**2, s**2))
print(points)
draw(Points(*points))
