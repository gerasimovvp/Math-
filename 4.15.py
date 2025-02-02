from vector_drawing import *
from add import add
import numpy as np 
import random
from math import pi
from vectors import scale, add, to_polar, to_cartesian
from hypothesis import given, strategies as st
from hypothesis.strategies import text


dimensions = 3

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
    return x, round(new_y, 4), round(new_z, 4)

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

def transform(pair):
    new_pair = []
    for vector in pair:
        new_pair.append(rotate_x_by(pi/2)(vector))
    return new_pair

def square(vec):
    return tuple(x**2 for x in vec)


def createVector(dimensions):
    vector = []
    for i in range(dimensions):
        vector.append(random.randint(0, 100))
    return tuple(vector)

def createPair():
    pair = []
    for i in range(2):
        pair.append(createVector(3))


@given(x1 = st.tuples(st.integers(0, 999), st.integers(0, 999), st.integers(0, 999)), x2 = st.tuples(st.integers(0, 999), st.integers(0, 999), st.integers(0, 999)))
def test1(x1, x2):
    assert(add(*transform((x1, x2))) == rotate_x_by(pi/2)(add(*((x1, x2)))))

@given(x1 = st.integers(0, 999), x2 = st.tuples(st.integers(0, 999), st.integers(0, 999), st.integers(0, 999)))
def test2(x1, x2):
    assert(rotate_x_by(pi/2)(scale(x1, x2)) == scale(x1, rotate_x_by(pi/2)(x2)))

@given(x1 = st.integers(0, 999), x2 = st.tuples(st.integers(0, 999), st.integers(0, 999), st.integers(0, 999)))
def test3(x1, x2):
    print((x1, x2))
    assert(square(scale(x1, x2)) == scale(x1, square(x2)))

test1()
test2()
test3()    

