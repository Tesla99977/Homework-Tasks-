a = int(input())
b = a%4
if a<=36 and  b/2 == 0 or a%2==0:
    print("Купе верхнее")
elif a<=36 and b/2 == 1 or a%2==1:
    print("Купе нижнее")
elif a>36 and b/2 == 0:
    print("Верхнее боковое")
else:
    print("Нижнее боковое")
    
