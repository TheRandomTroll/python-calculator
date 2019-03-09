def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

class Calculator:
    def __init__(self):
        print("Hello world")

    def execute(self, operation, a, b):
        if operation == '+':
            print(add(a, b))
        elif operation == '-':
            print(subtract(a, b))



c = Calculator()
c.execute('+', 3, 4)
