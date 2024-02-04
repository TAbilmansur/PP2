class Shape:
    def __init__(self):
        self.Area = 0
    def area(self):
        print(self.Area)
class Square(Shape):
    def __init__(self,length):
        self.Area = length**2
five = Square(5)
five.area()