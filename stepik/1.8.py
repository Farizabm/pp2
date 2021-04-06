'''x=int(input())
y=int(input())
print((x*60)+y)

X=int(input())
a=X//60
print(a)
print(X-(a*60))
'''
X=int(input())
H=int(input())
M=int(input())
a=X//60
b=X-(a*60)
b1=M+b
if(b1>=60):
    c=b1//60
    b1-=(c*60)
    a+=c
print(H+a)
print(b1)

