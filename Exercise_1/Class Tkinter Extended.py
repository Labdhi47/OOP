from tkinter import*
# Question 1
class TK_extended(Tk):

    def __init__(self, master , title):
        self.master = master
        self.title = title
    #------------    
    # Question 2 
    #------------
    def create(self):
        self.master = Tk()
        self.master.title(self.title)        
    
    #------------    
    # Question 3 
    #------------        
    def resize(self, width , height):
        self.master.geometry("{}x{}".format(width , height))
       
    #------------    
    # Question 4 
    #------------     
    def generate(self):
        self.master.mainloop() 
        
        
#------------    
# Execution 
#------------        
root = TK_extended("win" , "My Window")
root.create()
root.resize(500 , 300)
root.generate()