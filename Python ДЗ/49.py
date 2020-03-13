import random
b = random.randint(1,20)
a = [random.randint(-10,10) for i in range (0,b)]
print(a)
k=0
for j in range(0,b-1):
    if a[j]==a[j+1]==0:
        k+=1
print(a)
if k>0:
    print("Имеются два нуля подряд")
    
