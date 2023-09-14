class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        
    def sum_of_numbers(self):
        return f"Sum is : {self.num1 + self.num2}"   
    
    def substraction_of_numbers(self):
        return f"Substraction is : {self.num1 - self.num2}"
    
    def division_of_numbers(self):
        return f"Division is : {self.num1 / self.num2}"
    
    def multiplication_of_numbers(self):
        return f"Multiplication is : {self.num1 * self.num2}"
    
calculator = Calculator(3,2)
print(calculator.sum_of_numbers())
print(calculator.substraction_of_numbers())
print(calculator.division_of_numbers())
print(calculator.multiplication_of_numbers())
