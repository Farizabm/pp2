a = input()
a_list = list(map(str, input().split()))
a = len(a_list)

b = input()
b_list = list(map(str, input().split()))
b = len(b_list)

# s = students
missedstudents = list()
for s in a_list:
  if s not in b_list:
    missedstudents.append(s)
    print("Missed students: ", "\n - " , s)

notinthegroup = list()
for s in b_list:
  if s not in a_list:
    notinthegroup.append(s)
    print("Not in the group: ", "\n - " , s)                 






"""
3
Alik Darkhan Bekbolat
3
Alik Nurbergen Darkhan


Missed students:
- Bekbolat
Not in the group:
- Nurbergen
"""
