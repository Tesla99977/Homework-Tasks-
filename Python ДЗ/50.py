import random
b = random.randint(1,20)
a = [random.randint(-10,10) for i in range(0,b)]
print(a)
z = 0
k = 0
n = 0
for j in range (0,b):
    if a[j]//3==0 or -(a[j])//3==0:
        k+=1
    if a[j]>0:
        z=z+a[j]
        n+=1
        m = z//n
if m>0:
    a.append(m)
a.insert(0,k)
print(a)
