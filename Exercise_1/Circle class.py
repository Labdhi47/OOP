from math import pi

class Circle:
    def __init__(self,a,b,r):
        self.a = a         
        self.b = b         
        self.r = r

    def Area(self):
        return pi * self.r * self.r 

    def Perimeter(self):
        return 2 * pi * self.r 

    def equation(self,x,y):
        return (x-self.a)**2 + (y-self.b)**2 - self.r**2

    def test(self,x,y):
        if self.equation(x,y)==0:
            print("True")
        else:
            print("False")

Circle1=Circle(2,3,4)
print(Circle1.Perimeter())
print(Circle1.Area())
Circle1.test(1,2)
