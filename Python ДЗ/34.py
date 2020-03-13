a = [1,2,3,4,5,6]
b = 6
j=0
c = b//2
for i in range(0,b):
    a[i],a[c+i]=a[c+i],a[i]

print(a)
    
    
