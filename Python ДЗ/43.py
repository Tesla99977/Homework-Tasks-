a = [1,-2,3,4,-5,-6]
n = 6
b=[]
c=[]
k = 0
for i in range (0,n):
    if a[i]>0:
        k = a[i]
        b.append(k)
    elif a[i]<0:
        k = a[i]
        c.append(k)
print(b,c)
