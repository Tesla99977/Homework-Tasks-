a = [1,2,3,4,5,6,7,8]
b = 8
for i in range(0,b-1):
    if i%2==0 and i>0:
        a[i],a[i-1]=a[i-1],a[i]
print(a)
