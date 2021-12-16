a=input("put in number")
b=input("put in number")
c=input("put in number")
d=input("put in number")
a=int(a)
b=int(b)
c=int(c)
d=int(d)
count=0
count2=0
if a<0:
    count+=1
if a>0:
    count2+=1
if b<0:
    count+=1
if b>0:
    count2+=1
if c<0:
    count+=1
if c>0:
    count2+=1
if d<0:
    count+=1
if d>0:
    count2+=1
print("there are",count2,"positive and",count,"negative numbers")