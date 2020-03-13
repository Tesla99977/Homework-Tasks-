P = int(input())
H = int(input())
c = []
j=0
k=1
l=0
while j >-1:
    a = int(input())
    c.append(a)
    if c[j]==P or c[j]==H:
        break
    if c[j]>H:
        k = k*c[j]
    if c[j]<P:
        l = l+c[j]
    j+=1
print(k,l)
