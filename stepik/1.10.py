'''
A=int(input())
B=int(input())
H=int(input())
if H>=A and H<=B:
    print('Это нормально')
elif H<A and H<B:
    print('Недосып')
elif H>B and H>A:
    print('Пересып')
    '''
n=int(input())
if (n%4==0) and (n%100!=0) or (n%400==0):
    print('Високосный')
else:
    print('Обычный')