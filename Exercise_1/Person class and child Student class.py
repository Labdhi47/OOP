class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(f"Age is:{self.age} \nName is:{self.name}") 

class Student(Person):
    def __init__(self,name,age,section):
        Person.__init__(self,name,age)
        self.section=section

    def displayStudent(self):
        print(f"Age is:{self.age} \nName is:{self.name}\nSection is:{self.section}")    

P = Person("Tomas Wild", 37)
P.display()

Student1=Student("Labdhi","20","IT")
Student1.displayStudent()