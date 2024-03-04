txt = "NumbER of LOwerCaSe"
upper = sum(1 for c in txt if c.isupper())
lower = sum(1 for c in txt if c.islower())
print(upper,lower)