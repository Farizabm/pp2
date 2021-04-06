def finalPosition(move):
     
    l = len(move)
    Up, Down = 0, 0
    Left, Right = 0, 0

    for i in range(l):
        if (move[i] == 'U'):
            Up += 1
 
        elif(move[i] == 'D'):
            Down += 1
 
        elif(move[i] == 'L'):
            Left += 1
 
        elif(move[i] == 'R'):
            Right += 1
 
    print("Final Position: (", (Right - Left),
          ", ", (Up - Down), ")")
 
if _name_ == '_main_':
    #move = "UDDLLRUUUDUURUDDUULLDRRRR"
    move = "LURDRR"
    finalPosition(move)
 

#Output: Final Position: (2, 3)
