with open('03_04_02_input.txt') as in_f_obj:
    string = in_f_obj.readline().strip()
	
char = string[i]
i += 1

while i < len(string):    
	
	while string[i] in digits:
		multiplier += string[i]
		i += 1
		if i > (len(string) - 1):
			break
	
	#print(char * int(multiplier), end='')
	decrypted += (char * int(multiplier))
   
	multiplier = '' 
	if i > (len(string) - 1):
			break
	char = string[i]
	
	i += 1	

with open('03_04_02_ouput.txt', 'w') as out_f_obj:
	out_f_obj.write(decrypted)