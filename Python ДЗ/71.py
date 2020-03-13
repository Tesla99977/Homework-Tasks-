import random
N = int(input())
M = int(input())
z = 0
m=0
b=10
for i in range (N):
    a = [random.randint(0,10) for j in range(M)]
    for k in range(M):
        z=a[k]+z
    m = z/M  
    a.append(m)                            #Какая то средняя
    z = 0
    print(a)
