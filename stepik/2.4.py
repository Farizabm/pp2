'''
a=str(input())
x=len(a)
y1=a.upper().count('g'.upper())
y2=a.upper().count('c'.upper())
y=y1+y2
s=(y/x)*100
print(s)
'''
'''
a=str(input())
counter=1
for i in a:
    if i==a[1:-1]:
        counter+=1
        print(i, end='')
    else: 
        print(i, end='')
        print(counter, end='')
        counter=1
        '''
s = str(input())
l = len(s)-1
c = 1
t = ''
if len(s)==1:
    t = t +s+str(c)
else:
    for i in range(0,l):
        if s[i]==s[i+1]:
            c +=1
        elif s[i]!=s[i+1]:
            t = t + s[i]+str(c)
            c = 1
    for j in range(l,l+1):
        if s[-1]==s[-2]:
            t = t +s[j]+str(c)
        elif s[-1]!=s[-2]:
            t = t +s[j]+str(c)
            c = 1
print(t)