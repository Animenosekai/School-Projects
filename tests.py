from cProfile import run

### math.sqrt vs x**0.5

from math import sqrt

R = 100000000

def test1():
    for i in range(R):
        sqrt(i)

def test2():
    for i in range(R):
        i ** 0.5


run("test1()")
run("test2()")