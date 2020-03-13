a = input(int())
b = input(int())
c = input(int())
if a>b and b>c:
    print("max-", a,"min-",c)
if a>c and b<c:
    print("max-", a,"min-",b)
if a<b and a>c:
    print("max-", b,"min-",c)
if c<b and c>a:
    print("max-", b,"min-",a)
if c>b and b>a:
    print("max-", c,"min-",a)
if c>a and a>b:
    print("max-", c,"min-",b)
