a = []
j = 0
k = 0
B = int(input())
while j>-1:
    c = int(input())
    a.append(c)
    if a[j]%B==0:
        k = k+a[j]
        
    if a[j]<0:
        print(k)
        break
    j+=1
