def AND(x,y):
    return x*y

def OR(x,y):
    z=x+y
    if z>1:
        z=1
    return z

def XOR(x,y):
    if x==y:
        z=0
    else:
        z=1
    return z
A=input()
A=int(A)
B=input()
B=int(B)
C=input()
C=int(C)
D=input()
D=int(D)

F= AND(XOR(A,C),XOR(B,D))
print(F)
