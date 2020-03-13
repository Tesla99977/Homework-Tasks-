c=[]
j = 0
k = 0
m = 0
while j>-1:
    a = int(input())
    c.append(a)
    if c[j]<0:
        break
    elif j%2==0 or j ==0:
        k = c[j]**2+k
    else:
        m = -(c[j])+m
    j+=1
print(k,m)
