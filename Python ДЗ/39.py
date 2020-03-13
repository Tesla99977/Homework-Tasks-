a = [1,2,3,4,5,6,0]
b = 7
i = 0
while i <=b-1:
    temp=a[i]
    if temp==0:
        a.pop(i)
    i+=1
print(a)
