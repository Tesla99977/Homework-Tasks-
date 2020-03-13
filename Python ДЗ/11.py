print("Введите размер коробки A,B,C")
a = int(input())
b = int(input())
c = int(input())
print("Введите размер двери M, K")
m = int(input())
k = int(input())
if a*b >= m*k or a*c  >= m*k or b*c >= m*k:
    print ("Коробка проходит")
else:
    print( "Не проходит")
