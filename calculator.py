import trigonometry as trigonometry

class Calculator:
    def __init__(self):
        print("Hello world")

    def execute(self, operation, a, b):
        if operation == 'tan':
            print(trigonometry.tan(a))
        elif operation == '-':
            print(subtract(a, b))



c = Calculator()
c.execute('+', 3, 4)
