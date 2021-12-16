x=input("put in city please")
y=input("put in city please")
if (x=="Berlin" and y=="Peter") or (x=="Peter" and y=="Berlin"):
    print("no")
elif (x=="Berlin") or (y=="Peter"):
    print("yes")