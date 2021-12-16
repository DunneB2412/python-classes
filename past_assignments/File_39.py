x=input("put in password")
a=len(x)
if a<8:
    print("password has to have atleast 8 symbols")
else:
    y=input("put in passwort again")
    if x!=y: 
        print("passwords don't match!")  
    else:
        print("OK")