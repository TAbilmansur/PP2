class Point:
    def __init__(self,x = 0,y = 0,z = 0):
        self.move(x,y,z)
    def show(self):
        print(self.x,self.y,self.z)
    def move(self,x = 0,y = 0,z = 0):
        self.x,self.y,self.z = x,y,z
    def dist(self,point2):
        print(((self.x-point2.x)**2+(self.y-point2.y)**2+(self.z-point2.z)**2)**0.5)
p1 = Point(1,2,3)
p1.show()
p1.move(3,2,1)
p1.show()
p2 = Point(3,3,3)
p1.dist(p2)