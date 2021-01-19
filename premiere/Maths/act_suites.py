

### Activité 4
# Un placement financier
print("Un placement financier")

def Cn(n) -> float:
    """
    n is the number of years forward
    """
    c = 1000
    print(f"[Balance] 2016: 1000")
    for year in range(2017, n + 2017):
        c = c * 1.04 + 100
        print(f"[Balance] {str(year)}: {str(c)}")
    return c

Cn(15)


# Un peu de géométrie
print("")
print("Un peu de géométrie")
from math import sqrt
def geometry(n) -> float:
    """
    n is the final index number
    """
    d = 1
    print(f"Index 0: 1")
    for index in range(1, n + 1):
        d = sqrt(1 + d**2)
        print(f"Index {str(index)}: {str(d)}")

    return d

geometry(10)