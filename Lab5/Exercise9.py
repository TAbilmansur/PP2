import re 
s = input()
def AddSpace(a):
    return ' '+a.group(0)+' '
print((re.sub('[A-Z][a-z]*',AddSpace,s)).strip())