class Calculator:
    def addition(self, x, y):
        try:
            result = x + y
            return result
        except Exception as e:
            print("An error occurred during addition:", e)

    def subtraction(self, x, y):
        try:
            result = x - y
            return result
        except Exception as e:
            print("An error occurred during subtraction:", e)

    def multiplication(self, x, y):
        try:
            result = x * y
            return result
        except Exception as e:
            print("An error occurred during multiplication:", e)

    def division(self, x, y):
        try:
            result = x / y
            return result
        except ZeroDivisionError:
            print("Cannot divide by zero!")
        except Exception as e:
            print("An error occurred during division:", e)

    def exponentiation(self, x, y):
        try:
            if y < 0:
                raise ValueError("Exponent should be non-negative.")
            result = x ** y
            return result
        except ValueError as ve:
            print("An error occurred during exponentiation:", ve)
        except Exception as e:
            print("An error occurred during exponentiation:", e)

    def square_root(self, x):
        try:
            if x < 0:
                raise ValueError("Square root of a negative number is undefined.")
            result = x ** 0.5
            return result
        except ValueError as ve:
            print("An error occurred during square root operation:", ve)
        except Exception as e:
            print("An error occurred during square root operation:", e)

calc = Calculator()

print("Addition:", calc.addition(10, 5))
print("Subtraction:", calc.subtraction(10, 5))
print("Multiplication:", calc.multiplication(10, 5))
print("Division:", calc.division(10, 0))
print("Exponentiation:", calc.exponentiation(2, -3))
print("Square Root:", calc.square_root(-16))
