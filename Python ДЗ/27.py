import math
a = float(input())
if a<=0:
    print("0")
if 0< a <1:
    print(a**2-a)
if a>=1:
    print(a**2 - math.sin(3.14*(a**2)))
