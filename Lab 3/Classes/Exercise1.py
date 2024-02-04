class str_in_out:
    def getString(self):
        self.string = input()
    def printString(self):
        print(self.string)
s = str_in_out()
while (True):
    ans = input()
    if (ans == "in"):
        s.getString()
    else:
        s.printString()