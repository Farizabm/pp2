txt=str(input())
word=str(input())
pos=txt.find(word)
if word in txt:
    print("First time",word,'occured in position:',pos)
else:
    print('Not found')    