a = int(input())
h = int(input())
r = int(input())
m = int(input())
v1= a**3
v2= 3.14 * (r**2) * h
if v1 >= m:
    print("Входит в кубическую ёмкость")
else:
    print ("Не входит в кубическую")
if v2 >= m:
    print("Входит в цилиндрическую ёмкость")
else:
    print("Не входит в цилиндрическую")

