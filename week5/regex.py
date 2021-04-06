import re 
txt=str(input())

def match(text): 
          
        # regex 
        pattern = '[A-Z]+[a-z]+$'
          
        # searching pattern 
        if re.search(pattern, text): 
          print('Found a match!') 
        else: 
          print('Not matched!')
match(txt)