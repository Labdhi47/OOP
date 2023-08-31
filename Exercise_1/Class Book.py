class Book:
    def __init__(self):

        self.Title=input("Enter the Title:")
        self.Author=input("Enter the Author:")
        self.Price=input("Enter the Price:")

    def View(self):
        print(f"Title:{self.Title} \nAuthor:{self.Author} \nPrice:{self.Price}") 

Book1=Book()
Book1.View()