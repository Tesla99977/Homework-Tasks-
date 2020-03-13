a = [1,2,3,4,5,6,7]
N = 6
M = 2
K = int(input())
P = int(input())
i = P
j = K
while P<=i<=(P+M-1) and K<=j<=(K+M-1): 
    a[i],a[j]=a[j],a[i]
    i+=1
    j+=1
print(a)
