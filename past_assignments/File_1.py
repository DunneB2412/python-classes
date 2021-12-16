A=input("put in number")
B=input("put in number")
A=int(A)
B=int(B)
if A<B:
    print(A,B)
if B<A:
    x=A
    A=B
    B=x
    print(A,B)