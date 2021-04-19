import re
txt=str(input())
def matching(text):
     pattern='^[a-zA-Z0-9_]*$'
     if re.search(pattern,text):
          print("Found a match!")
     else:
          print("Not matched")  
matching(txt)             
  