a = int(input())
j=a%500
j1=a//500 
i=j%100
i1=j//100
g=i%10        
g1=i//10
k=g%2
k1=g//2
if a>=500:
    print("500 руб - ", j1)
if j<499 and j>99:
    print("100 руб - ", i1)
if i<99 and i>9:
    print("10 руб - ", g1)
if g<9:
    print("2 руб - ", k1)
else:
    print("+1")  
