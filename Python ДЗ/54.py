M = int(input())
p=0
for i in range(M):
    a = str(input())
    b = str(input())
    for j in range (len(a)-1):
        if a[j]==b[0] and a[j+1]==b[1]:
            p=p+1
    print(p)    
    p = 0    
