class Calculator:   #Class creation
    def __init__(self, a, b):   #Intilization
        self.a = a
        self.b = b

    def add(self):    #Add
        return self.a + self.b

    def subtract(self): #sub
        return self.a - self.b

    def multiply(self): #Mul
        return self.a * self.b

    def divide(self):  #Div
        if self.b != 0:
            return self.a / self.b
        else:
            return "Error: Division by zero"

#inputs
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
operator = input("Enter the type of operator (+, -, *, /): ")

# Instance creation
calculator = Calculator(a, b)

# Operations
if operator == '+':
    result = calculator.add()
elif operator == '-':
    result = calculator.subtract()
elif operator == '*':
    result = calculator.multiply()
elif operator == '/':
    result = calculator.divide()
else:
    result = "Error: Invalid operator"

#Result Display
print("Result:",str(round(result,6)))
