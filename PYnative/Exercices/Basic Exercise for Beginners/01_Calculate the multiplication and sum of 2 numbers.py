"""
Exercise 1: Calculate the multiplication and sum of two numbers
Given two integer numbers, write a Python program to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
"""

import numpy as np
from dataclasses import dataclass


# Shared logic
def compute_values(num1: int, num2: int) -> tuple[int, int]:
    product = num1 * num2
    suma = num1 + num2
    return product, suma


# Threshold variable
var = 1000


# 1. If Statement
def func1(num1: int, num2: int) -> str:
    product, suma = compute_values(num1, num2)
    if product <= var:
        return f"The result is {product}"
    return f"The result is {suma}"


# 2. Ternary Operator
def func2(num1: int, num2: int) -> str:
    product, suma = compute_values(num1, num2)
    return f"The result is {product}" if product <= var else f"The result is {suma}"


# 3. Min/Max Logic
def func3(num1: int, num2: int) -> str:
    product = num1 * num2
    suma = num1 + num2
    result = product if product <= var else suma
    return f"The result is {result}"


# 4. Lambda Function
func4 = lambda num1, num2: (
    f"The result is {num1 * num2}"
    if num1 * num2 <= var
    else f"The result is {num1 + num2}"
)


# 5. Class-Based Approach
class Processor:
    def __init__(self, num1: int, num2: int):
        self.num1 = num1
        self.num2 = num2

    def compute(self) -> str:
        product, suma = compute_values(self.num1, self.num2)
        if product <= var:
            return f"The result is {product}"
        return f"The result is {suma}"


def func5(num1: int, num2: int) -> str:
    return Processor(num1, num2).compute()


# 6. Pattern Matching (Python 3.10+)
def func6(num1: int, num2: int) -> str:
    product, suma = compute_values(num1, num2)
    match product:
        case i if i <= var:
            return f"The result is {i}"
        case _:
            return f"The result is {suma}"


# 7. Dictionary-Based Dispatch
def func7(num1: int, num2: int) -> str:
    product, suma = compute_values(num1, num2)
    return {True: f"The result is {product}", False: f"The result is {suma}"}[
        product <= var
    ]


# 8. Try-Except Handling
def func8(num1: int, num2: int) -> str:
    try:
        product = num1 * num2
        if product <= var:
            return f"The result is {product}"
        else:
            return f"The result is {num1 + num2}"
    except Exception as e:
        return f"Error: {e}"


# 9. NumPy-Based
def func9(num1: int, num2: int) -> str:
    product = np.multiply(num1, num2)
    suma = np.add(num1, num2)
    return f"The result is {product}" if product <= var else f"The result is {suma}"


# 10. Generator Function
def func10(num1: int, num2: int) -> str:
    def generate_result():
        product = num1 * num2
        yield (
            f"The result is {product}"
            if product <= var
            else f"The result is {num1 + num2}"
        )

    return next(generate_result())


# 11. Functional Programming with map
def func11(num1: int, num2: int) -> str:
    product, suma = map(
        lambda x: x(num1, num2), [lambda x, y: x * y, lambda x, y: x + y]
    )
    return f"The result is {product}" if product <= var else f"The result is {suma}"


# 12. Dataclass-Based
@dataclass
class Numbers:
    num1: int
    num2: int

    def result(self) -> str:
        product = self.num1 * self.num2
        suma = self.num1 + self.num2
        return f"The result is {product}" if product <= var else f"The result is {suma}"


def func12(num1: int, num2: int) -> str:
    return Numbers(num1, num2).result()


# Test Runner
def versions(func, label):
    print(label)
    print(func(20, 30))  # product = 600
    print(func(40, 30))  # product = 1200
    print("-------------------------------------")


# Run all versions
versions(func1, "1. If Statement")
versions(func2, "2. Ternary Operator")
versions(func3, "3. Min/Max Logic")
versions(func4, "4. Lambda Function")
versions(func5, "5. Class-Based Approach")
versions(func6, "6. Pattern Matching")
versions(func7, "7. Dictionary-Based Dispatch")
versions(func8, "8. Try-Except Handling")
versions(func9, "9. NumPy-Based")
versions(func10, "10. Generator Function")
versions(func11, "11. Functional Programming with map")
versions(func12, "12. Dataclass-Based")
