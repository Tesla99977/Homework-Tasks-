M = int(input())
b = 0
for i in range(M):
    k = str(input())
    for m in range(len(k)):
        print(k[m])
        c = str(k[m])
        if c == "а" or c=="и" or c == "е" or c== "о" or c== "у" or c== "э" or c=="ю" or c== "я":
            b=b+1
    print(b)
    b = 0    
    
