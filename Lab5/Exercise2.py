import re 
s = input()
print(re.findall('ab{2,3}',s))