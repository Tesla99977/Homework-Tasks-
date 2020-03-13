import random
N = int(input())
M = int(input())
k = 0
p=10
z = 0
for i in range(N):
    a = [random.randint(0,10)for j in range(M)]
    print(a)
    for n in range(M):
        k=a[n]+k        #Cумма
    if k>z:
        z=k
    k=0
for m in range(M):
    if a[m]<p:
        p=a[m]
        y=m
print(a[y])
