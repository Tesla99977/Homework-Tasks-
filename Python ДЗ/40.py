a = [1,-2,3,-4,-5,6]
b = 6
i = 0
while i<= len(a) :
    if a[i]<0:
        temp1 = a[i]
        temp = temp1*temp1
        a.insert( i+1,temp)
    i+=1
print(a)
