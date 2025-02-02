from vectors import *

def matrix_multiply(a, b):
    return tuple(
        tuple(dot(row, col) for col in zip(*b)) for row in a
    )

a = ((1,1,0), (1,0,1), (1,-1,1))
b = ((0,2,1), (0,1,0), (1,0,-1))

print(matrix_multiply(a,b))

c = ((1,2), (3,4))
d = ((0,-1),(1,0))

print(matrix_multiply(c,d))