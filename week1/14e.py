import math
s=str(input())
if s=='треугольник':
    a=int(input())
    b=int(input())
    c=int(input())
    p = (a+b+c)/2
    S = math.sqrt(p * (p-a) * (p-b) * (p-c))
    print(S)
if s=='прямоугольник':
    a=int(input())
    b=int(input())   
    A=a*b
    print(A)
if s=='круг':
    r=int(input())
    Ar=3.14*r**2
    print(Ar)





    
