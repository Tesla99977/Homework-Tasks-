a = [-1,-2,-3,4,-5,6]
b = 6
plus = 0
minus = 0
for i in range (0,b):
    if a[i]>0:
        plus= plus+a[i]
    if a[i]<0:
        minus = minus+(-(a[i]))
if minus<plus:
    k = plus-minus
    a.append(-k)
if plus<minus:
    k = minus-plus
    a.append(k)
print (a)
