b = int(input())
a = []
x = 0
for i in range (0,b):
    c = list(input())
    a.append(c)
    if len(c)>x :
          x = len(c)
for j in range (0,b-1):
    if len(a[j])<x:
      while len(a[j])<x:
          a[j]+="*"
print(a)
    
