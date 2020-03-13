x = float(input())
y = float(input())
z = float(input())
if x+y>z and x+z>y and y+z>x:
    if x**2+y**2==z**2 or x**2+z**2==y**2 or y**2+z**2==x**2:
        print("Треугольник прямоугольный")
    else:
        print("Треугольник существует")
else:
    print("Не существует")
