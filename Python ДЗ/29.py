a = int(input())
b=a//100
if a%4==0 and a%100>0:
 print("Високосный, век -",b+1)
elif a % 400 ==0:
  print("Високосный,век- ",b+1)
else:
  print ("Обычный, век- ",b+1)
