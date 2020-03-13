a = [23,45,67,-10,20,-35]
b = 6
T = 10
for i in range (0,b):
    if a[i]>0:
        c = a[i]//T
        a[i]=c
print(a)
