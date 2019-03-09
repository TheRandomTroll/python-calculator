def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

class Calculator:
    def execute(self, operation, a, b):
        if operation == '+':
            add(a, b)
        elif operation == '-':
            subtract(a, b)
        elif operation == '*':
            multiply(a, b)
        elif(operation == '/'):
            divide(a, b)





c = Calculator()
c.execute('+', 3, 4)
