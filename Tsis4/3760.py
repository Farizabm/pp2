n = int(input())
dict = []

for i in range(n):
 dict.append(list(input().split()))

search = input()
for word in dict:
 if word[0] == search:
   print(word[1])
 elif word[1] == search:
   print(word[0])