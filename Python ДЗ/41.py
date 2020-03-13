a = [1,3,2,4,5,-1]
b = 6 
d= 0
for i in range (0,b):
    if a[i]<0:
        for j in range(i-1,0,-1):
            temp = a[j]
            if temp>a[j-1]:
                temp = a[j]
                d = 1
            else:
                d = 0
                break
            
if d == 1:
    print("Возрастает")
else:
    print("Убывает")
