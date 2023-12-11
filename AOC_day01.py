import re
lines = open('input.txt', 'r').readlines()

sum = 0
for line in lines:
    digits_only = re.sub('\D','',line)
    sum += int(digits_only[0] + digits_only[-1])
print(sum) #Part 1


sum = 0
digits = {'one' : 'on1e', 'two' : 'tw2o', 'three' : 'thr3e','four': 'fo4ur', 'five':'fi5ve','six': 'si6x','seven': 'sev7en','eight' : 
'ei8ght','nine':'ni9ne'}
for line in lines:
    for key,value in digits.items():
        line = line.replace(key, value)
    
    str = re.sub('\D','',line)
    sum += int(str[0] + str[-1])
print(sum) #Part 2


