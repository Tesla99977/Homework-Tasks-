import random
N = int(input())
M = int(input())
z = 0
m=0
b=0
for i in range (N):
    a = [random.randint(0,10) for j in range(M)]
    print(a)
    for k in range(M):
        z=a[k]+z
    m = z/M             #Какая та средняя
    z = 0
    if m>b:
        b=m
        m=0
    m=0
print(b)
