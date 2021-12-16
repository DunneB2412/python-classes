import abc


x=input("put in number")
x=int(x)
a=x//100
b=x//10%10
c=x%10
a=int(a)
b=int(b)
c=int(c)
if a!=b!=c:
    print("OK")
else:
    print("there are several same numbers")
