import re 
s = input()
def Snake_to_Camel(a):
    return a.group(0).upper()[1::]
print(re.sub('_[a-z]',Snake_to_Camel,s))