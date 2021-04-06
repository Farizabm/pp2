'''
from math import sqrt
a=int(input())
b=int(input())
c=int(input())
p=(a+b+c)/2
s=p*(p-a)*(p-b)*(p-c)
S=sqrt(s)
print(S)
'''
'''
a=int(input())
if (a>-15 and a<=12) or( a>14 and a<17) or (a>=19):
    print(True)
else:
    print(False)
    '''
'''
a=float(input())
b=float(input())
c=str(input())
if c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="*":
    print(a*b)
elif c=="/":
    if b==0:
        print("Деление на 0!")
    else:
        print(a/b)
elif c=="mod":
    if b==0:
        print("Деление на 0!")
    else:
        print(a%b)
elif c=="pow":
    print(a**b)
elif c=="div":
    if b==0:
        print("Деление на 0!")
    else:
        print(a//b)
'''
'''
from math import sqrt
n=str(input())
if n=="треугольник":
    a=int(input())
    b=int(input())
    c=int(input())
    p=float((a+b+c)/2)
    s=float(p*(p-a)*(p-b)*(p-c))
    S=float(sqrt(s))
    print(S)
elif n=="прямоугольник":
    a=int(input())
    b=int(input())
    print(float(a*b))
elif n=="круг":
    r=int(input())
    print(float(3.14*(r**2)))
    '''
'''
a=int(input())
b=int(input())
c=int(input())
s=a+b+c
print(max(a,b,c))
print(min(a,b,c))
print(s - max(a,b,c) - min(a,b,c))
'''
'''
s = int (input())
n1 =" программистов"
n2 =" программист"
n3 =" программиста"
if  s>=0:
  if s==0:
    print(str(s) + n1)
  elif s%100>=10 and s%100<=20:
    print(str(s) + n1)
  elif s%10==1:
    print(str(s) + n2)
  elif s%10>=2 and s%10<=4:
    print(str(s) + n3)
  else:
    print(str(s) + n1)
'''
'''
n=int(input())
a6=n%10
n=n//10
a5=n%10
n=n//10
a4=n%10
n=n//10
a3=n%10
n=n//10
a2=n%10
n=n//10
a1=n%10
n=n//10
S1=a1+a2+a3
S2=a4+a5+a6
if S1==S2:
    print("Счастливый")
else:
    print("Обычный")
    '''