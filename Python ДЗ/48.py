import random
b = random.randint(1,20)
a = [random.randint(0,10) for i in range(0,b)]
c = 0
print(a)
for j in range (0,b-1):
    if a[j]==0:
        a[j] = a[j-1]+a[j-2]
print(a)
