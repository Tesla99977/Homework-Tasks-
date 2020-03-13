a = [1,2,3,4,5,6]
b = 6
M = int(input())
K = int(input())
for i in range(K+M-1,K-1,-1):
    a.pop(i)
print(a)
