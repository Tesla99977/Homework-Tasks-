a = [1,-2,-3,-4,-5,-6]
b = 6
j=0
k=0
for i in range(0,b):
    if a[i]>0:
        j+=1
    if a[i]<0:
        k+=1
if j>k:
    for z in range(k,j):
        a.append(-(a[z]))
if k>j:
    for m in range(j,k):
        a.append((-a[m]))
print (a)
