A = int(input())
B = int(input())
H = int(input())
if (H>=A) and (H<=B) and (A<=B):
    print('Это нормально')
if (H<A) and (A<=B):
    print('Недосып')
if (H>B) and (A<=B):
    print('Пересып')