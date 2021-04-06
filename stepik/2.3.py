'''
n=int(input())
m=int(input())
s=int(input())
t=int(input())
for a in range(s,t+1):
    print('\t'+str(a),end='')
print(end='\n')
for i in range(n,m+1):
    print(str(i)+'\t',end='')
    for j in range(s,t+1):
        print(i*j ,end='\t')
    print()
    '''
a=int(input())
b=int(input())
s=0
n=0
for i in range(a,b+1):
    if i%3==0:
       s+=i
       n+=1
s/=n
print(s)