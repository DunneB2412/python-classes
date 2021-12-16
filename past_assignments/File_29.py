x=input("put in number")
y=input("put in number")
q=input("put in number")
x=int(x)
y=int(y)
q=int(q)
if x>y>q:
    print(x,y,q)
elif y>x>q:
    print(y,x,q)
elif q>y>x:
    print(q,y,x)
elif q>x>y:
    print(q,x,y)