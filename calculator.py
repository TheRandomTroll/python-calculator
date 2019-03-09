import basicarithmetic as basicarithmetic


class Calculator:
    def execute(self, operation, a, b):
        if operation == '+':
            basicarithmetic.add(a, b)
        elif operation == '-':
            basicarithmetic.subtract(a, b)
        elif operation == '*':
            basicarithmetic.multiply(a, b)
        elif(operation == '/'):
            basicarithmetic.divide(a, b)

c = Calculator()
c.execute('+', 3, 4)
