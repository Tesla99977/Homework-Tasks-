c=1
b=0
i =0
d=[]
while i >-1:
    a = int(input())
    if a == 55555:
        break
    if i//2==0 or i ==0:
        d.append(a)
        c = c*d[i]
    else:
        d.append(a)
        b = b+ d[i]
        
    i+=1
