import random
N = int(input())
M = int(input())
k = 0
z=0
for j in range(M):
    a = [random.randint(0,10)for i in range(N)]
    print(a)
    for m in range (N):
        
        k=a[m]+k
    if z<k:
        z=k
    k=0
print(z)
    
