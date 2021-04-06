'''
s=0
i=int(input())
while i!=0:
    s=s+i
    i=int(input())
print(s)
'''
'''
a=int(input())
b=int(input())
i=1
while i%a!=0 or i%b!=0:
    i+=1
print(i)
'''
i=0
while i<=100:
    i = int(input())
    if i>100:
        break
    if i<10:
        continue
    print(i)