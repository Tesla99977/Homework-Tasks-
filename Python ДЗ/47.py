import random
b = (random.randint(1,20))
a = [random.randint(-100,100)for i in range(b)]
B = -50
C = 40
print(a)
for j in range(0,b-1):
    if B<a[j]<C:
        a.pop(j)
print(a)
