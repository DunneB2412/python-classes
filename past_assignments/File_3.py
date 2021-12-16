a=input("put in number")
b=input("put in number")
a=int(a)
b=int(b)
if a!=b:
    a=a+b
    b=a
    print(a,b)
else:
    a=0
    b=0
    print(a,b)