a=input("put in number")
b=input("put in number")
c=input("put in number")
a=int(a)
b=int(b)
c=int(c)
if abs(a-b)<abs(a-c):
    print("b",abs(a-b))
elif abs(a-c)<abs(a-b):
    print("c",abs(a-c))
