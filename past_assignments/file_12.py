a=input("put in number")
b=input("put in number")
c=input("put in number")
a=float(a)
b=float(b)
c=float(c)
if a<b<c or a>b>c:
    print(a*2,b*2,c*2)
else:
    print(-a,-b,-c)