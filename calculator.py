import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def square_root(a):
    if a < 0:
        return "Error: Cannot calculate square root of a negative number!"
    return math.sqrt(a)

def advanced_calculate(expression):
    
    return eval(expression)

    

print("Addition (10 + 5):", add(10, 5))
print("Subtraction (10 - 5):", subtract(10, 5))
print("Multiplication (10 * 5):", multiply(10, 5))
print("Division (10 / 2):", divide(10, 2))
print("Square Root of 25:", square_root(25))


print("Advanced (10 + 5):", advanced_calculate("10 + 5"))
