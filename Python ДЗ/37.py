import array
a = [1,2,3,4,5,6]
b = 6
temp = 0
k=0
for i in range(0,b):
    temp = temp+a[i]
    if a[i]>0:
        k+=1

for j in range(b-1,-1,-1):    
    a.pop(j)
a.append(temp)
a.append(k)
print (a)
