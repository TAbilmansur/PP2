import re 
s = input()
def CamelToSnake(a):
    return '_'+a.group(0)[0].lower()
print((re.sub('[A-Z]',CamelToSnake,s)).strip())