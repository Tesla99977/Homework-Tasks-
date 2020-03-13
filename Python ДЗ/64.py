c = []
j=0
m = 0
while j>-1:
    a = int(input())
    c.append(a)
    if c[j]>0:
        m = m+c[j]
    if c[j]==0:
        print(m)
    if c[j]==99999:
        break


    j+=1
