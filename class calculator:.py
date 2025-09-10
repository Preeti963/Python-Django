class calculator:
    def  addition(self, a, b):
        return a + b
    def subtraction(self, a, b):
        return a-b
    def multiplication(self, a, b):
        return a * b
    def divide(self, a, b):
        return a/b 
    
calc = calculator()

print("addition:", calc.addition(10,5))
print("subtraction:",calc.subtraction(10,5))
print("multiplication:",calc.multiplication(10,5))
print("divide:",calc.divide(10,5))