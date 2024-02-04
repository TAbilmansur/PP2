class Shape:
    def __init__(self):
        self.Area = 0
    def area(self):
        print(self.Area)
class Square(Shape):
    def __init__(self,length):
        self.Area = length**2
class Rectangle(Shape):
    def CalculateArea(self):
        self.Area = self.length*self.width
    def __init__(self,length,width):
        self.length,self.width = length,width
        self.CalculateArea()
five = Rectangle(5,12)
five.area()