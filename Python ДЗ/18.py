a = int(input())
h = int(input())
r = int(input())
m = int(input())
v1= a**3
v2= 3.14 * (r**2) * h
if v1 == m:
    print("Заполнит кубическую ёмкость")
else:
    print ("Не заполнит кубическую")
if v2 == m:
    print("Заполнит цилиндрическую ёмкость")
else:
    print("Не заполнит цилиндрическую")

