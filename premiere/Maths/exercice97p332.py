"""
##### BEFORE OPTIMIZATION
from random import *

def sauts(n):
    p = 0
    k = 0
    for _ in range(1, n+1):
        d = randint(0, 1)
        if d == 0:
            p = p - 1
        else:
            p = p + 1
        if p == 0:
            k = k + 1
    return k
"""

##### AFTER OPTIMIZATION
from random import getrandbits
def sauts(n):
    p, k = 0, 0
    for _ in range(n):
        p = (p - 1 if getrandbits(1) == 0 else p + 1)
        if p == 0: k += 1
    return k

"""
class Counter():
    def __init__(self) -> None:
        self.data = 0

    def increase(self):
        self.data += 1
        return self.data
    def decrease(self):
        self.data -= 1
        return self.data

def sauts(n):
    p = Counter()
    return sum([(p.decrease() == 0 if getrandbits(1) == 0 else p.increase() == 0) for _ in range(n)])
"""
"""
def test():
    from time import time
    start = time()
    sum([sauts(i) == 0 for i in range(10000)])
    print(time() - start)
"""

def test():
    return sauts(1000000000)

import cProfile
cProfile.run("test()")