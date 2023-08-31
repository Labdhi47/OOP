class A:
	def __init__(self, n):
		self.name = n

class B(A):
	def __init__(self,name,roll):
        A.__init__(self,name)
        self.roll = roll

o= B("labdhi",3)
print(o.name)
