a =[]
j = 0
k = 0
m = 0
while j>-1:
    c = int(input())
    a.append(c)
    if a[j]==65432:
        print("Положительных =",(k/(k+m))*100,"%  ","Отрицательных = ", (m/(k+m))*100,"%")
    if a[j]>0:
        k = k+1
    if a[j]<0:
        m = m+1

    j+=1
