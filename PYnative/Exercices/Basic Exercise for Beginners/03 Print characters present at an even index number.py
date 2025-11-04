"""
Write a Python code to accept a string from the user and display characters present at an even index number.
For example, str = "PYnative", so yout code should display 'P', 'n', 't', 'v'.
"""

import numpy as np
from itertools import compress


# 1. Original
def func1(string):
    result = ""
    for i in range(len(string)):
        if i % 2 == 0:
            result += string[i]
    print(result)


# 2. Range() loop
def func2(string):
    result = ""
    for i in range(0, len(string), 2):
        result += string[i]
    print(result)


# 3. List comprehension
def func3(string):
    print("".join([char for i, char in enumerate(string) if i % 2 == 0]))


# 4. String slicing
def func4(string):
    print(string[::2])


# 5. Enumerate
def func5(string):
    result = ""
    for i, char in enumerate(string):
        if i % 2 == 0:
            result += char
    print(result)


# 6. Filter() and lambda (not recommended for repeated characters)
def func6(string):
    print("".join(filter(lambda x: string.index(x) % 2 == 0, string)))


# 7. Recursion
def func7(string, i=0):
    result = ""
    if i < len(string):
        result += string[i]
        print(result, end="")
        func7(string, i + 2)


# 8. map() with custom function
def func8(string):
    def func8_1(i):
        return string[i] if i % 2 == 0 else ""

    print("".join(map(func8_1, range(len(string)))))


# 9. NumPy
def func9(string):
    arr = np.array(list(string))
    print("".join(arr[::2]))


# 10. zip() with index range
def func10(string):
    result = ""
    for i, char in zip(range(len(string)), string):
        if i % 2 == 0:
            result += char
    print(result)


# 11. itertools.compress()
def func11(string):
    selectors = [i % 2 == 0 for i in range(len(string))]
    print("".join(compress(string, selectors)))


# Main function
def main_func(func, label):
    print(label)
    print("Printing only even index chars")
    func(string)
    print("-------------------------")


string = str(input("Original String is "))

main_func(func1, "1. Original")
main_func(func2, "2. range() loop")
main_func(func3, "3. List comprehension")
main_func(func4, "4. String slicing")
main_func(func5, "5. Enumerate")
main_func(func6, "6. filter() and lambda")
main_func(func7, "7. Recursion")
main_func(func8, "8. map() and custom function")
main_func(func9, "9. NumPy")
main_func(func10, "10. zip() with index range")
main_func(func11, "11. itertools.compress()")
