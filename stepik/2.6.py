'''
a= int(input())
s=a
s1=0+abs(a**2)
while s!=0:
    a=int(input())
    s=s+a
    s1=s1+abs(a)**2
    if s==0:
        break
print(s1)
'''
'''
a=int(input())
m=[]
for i in range(a):
    j=0
    while j<i+1:
        m.append(i+1)
        j+=1
    if len(m)>a: 
        break
m=m[0:a]
for i in m:
    print(i, end=" ")
    '''
'''
lst = [int(i) for i in input().split()]
x= int(input())
for i in range(len(lst)):
    if x==lst[i]:
        print(i,end=' ')
if x not in list:
    print('Отсутствует')
'''
def spiral(n):
    dx,dy = 1,0           
    x,y = 0,0              
    myarray = [[None]* n for j in range(n)]
    for i in range(1,n**2+1):
        myarray[x][y] = i
        nx,ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<n and myarray[nx][ny] == None:
            x,y = nx,ny
        else:
            dx,dy = -dy,dx
            x,y = x+dx, y+dy
    return myarray
def printspiral(myarray):
    n = range(len(myarray))
    for y in n:
        for x in n:
            print (myarray[x][y],end=' ')
        print()
n = int(input())
printspiral(spiral(n))
