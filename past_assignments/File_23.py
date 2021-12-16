x=input("put in year")
x=int(x)
if x%100==0 and x%400!=0:
    print("normal year")
elif x%4!=0:
    print("normal year")
else:
    print("leap year")