n=int(input())
v = []

for i in range(1, n+1):
    v += [str(i)] * i

print(" ".join(v[:n]))