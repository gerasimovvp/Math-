from teapot import load_triangles
from draw_model import draw_model
from vectors import scale, add, to_polar, to_cartesian
from functools import reduce
from math import pi

def scale2(v):
    return scale(2.0, v)

def translate1left(v):
    return add((-1,0,0), v)

def compose(*args):
    def new_function(input):
        state = input
        for func in reversed(args):
            state = func(state)
        return state
    return new_function

def scale_by(scalar):
    def new_function(v):
        return scale(scalar, v)
    return new_function

def translate_by(vec):
    def new_function(v):
        return add(vec, v)
    return new_function

def test(a, b):
    print("TEST: ", a, b)

def curry2(f):
    def f1(a):
        def f2(b):
            f(a, b) 
        return f2
    return f1

    

def polygon_map(transformation, polygons):
    return [
        [transformation(vertex) for vertex in triangle]
        for triangle in polygons
    ]    

def rotate2d(angle, vector):
    l,a = to_polar(vector)
    return to_cartesian((l, a+angle))

def rotate_z(angle, vector):
    x,y,z = vector
    new_x, new_y = rotate2d(angle, (x,y))
    return new_x, new_y, z

def rotate_z_by(angle):
    def new_function(v):
        return rotate_z(angle, v)
    return new_function

def rotate_x(angle, vector):
    x,y,z = vector
    new_z, new_y = rotate2d(angle, (z,y))
    return x, new_y, new_z

def rotate_x_by(angle):
    def new_function(v):
        return rotate_x(angle, v)
    return new_function

def rotate_y(angle, vector):
    x,y,z = vector
    new_x, new_z = rotate2d(angle, (x,z))
    return new_x, y, new_z

def rotate_y_by(angle):
    def new_function(v):
        return rotate_y(angle, v)
    return new_function

def stretch_x(num, vector):
    x,y,z = vector
    return(num*x, y, z)

def stretch_x_by(num):
    def new_function(v):
        return stretch_x(num, v)
    return new_function

scale2_then_translate1left = compose(translate_by((-1,0,0)), scale_by(2))
translate1left_then_scale2 = compose(scale_by(2), translate_by((-1,0,0)))
rotate = compose(rotate_z_by(pi/2), rotate_x_by(pi/2))

Ae1 = (1,1,-1)
Ae2 = (1,0,-1)
Ae3 = (0,1,1)

def apply_A(v):
    return add(
        scale(v[0], Ae1),
        scale(v[1], Ae2),
        scale(v[2], Ae3)
    )

def linear_combination(scalars, *vectors):
    # print(list(zip(scalars, vectors)))
    # print(sum(scale(i[0], i[1])))
    sum = (0,0,0)
    for i in zip(scalars, vectors):
        sum = add(sum, scale(i[0], i[1]))
    return sum


print(linear_combination([1,2,3], (1,0,0),(0,1,0),(0,0,1)))
####################################################################
#### this code takes a snapshot to reproduce the exact figure
#### shown in the book as an image saved in the "figs" directory
#### to run it, run this script with command line arg --snapshot
import sys
import camera
if '--snapshot' in sys.argv:
    camera.default_camera = camera.Camera('fig_4.4_draw_teapot',[0])
####################################################################
e1 = (1,0,0)
e2 = (0,1,0)
e3 = (0,0,1)

# print(rotate_x_by(pi/2)(e1))
# print(rotate_x_by(pi/2)(e2))
# print(rotate_x_by(pi/2)(e3))
# d = curry2(test)
# d("dd")("ff")
original_triangles = load_triangles()
draw_model(load_triangles())
#draw_model(polygon_map(scale_by(-1), load_triangles()))
#draw_model(polygon_map(translate_by((0,0,0)), load_triangles()))
#draw_model(polygon_map(scale2_then_translate1left, load_triangles()))
# draw_model(polygon_map(translate1left_then_scale2, load_triangles()))
#draw_model(polygon_map(rotate_z_by(pi/4.), load_triangles()))
#draw_model(polygon_map(stretch_x_by(2.), load_triangles()))
# draw_model(polygon_map(rotate, load_triangles()))
# draw_model(polygon_map(rotate_y_by(pi/2), load_triangles()))
# draw_model(polygon_map(apply_A, load_triangles()))
