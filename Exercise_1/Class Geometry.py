import math

class Geometry:

    def __init__(self):
        pass

    def distance(self,a,b):
        return math.sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2)

    def middle(self,a,b):
        return ((a[0]+b[0])/2),((a[1]+b[1])/2)

    def triangle_perimeter(self,a,b,c):
        return a+b+c

    def iscoceles(self,side_a,side_b,base):
        if side_a == side_b:
            return True
        else:
            return False
            
length = Geometry()
print(length.distance((2,3),(6,9)))
print(length.middle((2,3),(6,9)))
print(length.triangle_perimeter(2,3,2))
print (length.iscoceles(3,3,2))