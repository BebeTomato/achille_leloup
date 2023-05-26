#!/usr/bin/env python3
import sys

class Calculator:
    def __init__(self):
        self.memory = 0

    def add(self, a, b):
        result = a + b
        self.memory = result
        return result

    def subtract(self, a, b):
        result = a - b
        self.memory = result
        return result

    def multiply(self, a, b):
        result = a * b
        self.memory = result
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.memory = result
        return result

    def power(self, a, b):
        result = a ** b
        self.memory = result
        return result

    def sqrt(self, a):
        if a < 0:
            raise ValueError("Cannot calculate square root of a negative number")
        result = a ** 0.5
        self.memory = result
        return result

    def clear_memory(self):
        self.memory = 0

    def get_memory(self):
        return self.memory

#print for the tests
calc = Calculator()
result = calc.add(int(sys.argv[1]), int(sys.argv[2]))
print(result)
result = calc.subtract(int(sys.argv[1]), int(sys.argv[2]))
print(result)
result = calc.multiply(int(sys.argv[1]), int(sys.argv[2]))
print(result)
result = calc.divide(int(sys.argv[1]), int(sys.argv[2]))
print(result)
result = calc.power(int(sys.argv[1]), int(sys.argv[2]))
print(result)
"""result = calc.sqrt(int(sys.argv[1]), int(sys.argv[2]))
print(result)"""
