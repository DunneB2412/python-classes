a=input("put in number")
b=input("put in number")
c=input("put in number")
a=int(a)
b=int(b)
c=int(c)
if b<a<c or b>a>c:
    print(a)
if a<b<c or a>b>c:
    print(b)
if a<c<b or a>c>b:
    print(c)