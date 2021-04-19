x = [int(i) for i in input().split()]
y=int(input())
for i in range(len(x)):
    if((x[i])==y):
        print(i,end=' ')
    if y not in x:
        print('Отсутствует')
        break
    