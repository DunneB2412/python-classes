a=input("put in number")
b=input("put in number")
a=int(a)
b=int(b)
if a!=b and a<b:
    a=b
    print(a,b)
elif a!=b and a>b:
    b=a
    print(a,b)
else:
    a=0
    b=a
    print(a,b)