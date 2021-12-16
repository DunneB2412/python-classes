a=input("put in number")
b=input("put in number")
c=input("put in number")
a=int(a)
b=int(b)
c=int(c)
if b>a<c and a<b>c:
    print(a,b)
elif b>a<c and a<c>b:
    print(a,c)
elif a>b<c and a<c>b:
    print(b,c)
elif a>b<c and c<a>b:
    print(b,a)
elif a>c<b and c<a>b:
    print(c,a)
elif a>c<b and c<b>a:
    print(c,b)