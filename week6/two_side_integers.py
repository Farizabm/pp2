n = int(input())
a = input()
n = len(a)
k = int(input())

b = a[0:k]
c = a[k:0]

x = int("".join([str(i) for i in b]))
y = int("".join([str(i) for i in c]))

print(x*y)
"""
7
1 4 3 2 6 2 3
4
"""