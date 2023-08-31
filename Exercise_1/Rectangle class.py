class Rectangle:
    def __init__(self,height,width):
        self.height = height
        self.width = width

    def Perimeter(self):
        return 2*(self.height + self.width)   

    def Area(self):
        return self.height * self.width

    def display(self):
        print("Height:",self.height)
        print("Width:",self.width)
        print("Perimeter is:",self.Perimeter())
        print("Area is:",self.Area())

class Parallelepipede(Rectangle):
    def __init__(self,height,width,length):
        Rectangle.__init__(self,height,width)
        self.length = length

    def volume(self):
        print(f"Volume is:{self.height * self.width * self.length}")
    
R=Rectangle(7,5)
R.display()    

print("-------------------------")

P=Parallelepipede(7,5,2)
P.volume()       
