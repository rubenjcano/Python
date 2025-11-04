"""
Exercise 4: Remove first n characters from a string
Write a Python code to remove characters from a string from 0 to n and return a new string.
"""


# 1. String slicing
def func1(word, n):
    return word[n:]


# 2. Lambda function
func2 = lambda word, n: word[n:]


# 3. Negative indexing
def func3(word, n):
    return word[-(len(word) - n) :]
    # return word[n - len(word):]


# 4. Loop-based character removal
def func4(word, n):
    result = ""
    for i in range(n, len(word)):
        result += word[i]
    return result


# 5. List comprehension with str.join()
def func5(word, n):
    return "".join([char for i, char in enumerate(word) if i >= n])


# 6. Generator expression
def func6(word, n):
    return "".join(char for i, char in enumerate(word) if i >= n)


# 7. filter with range
def func7(word, n):
    return "".join([word[i] for i in filter(lambda x: x >= n, range(len(word)))])


# 8. zip() and enumerate()
def func8(word, n):
    return "".join([char for i, char in zip(range(len(word)), word) if i >= n])


# 9. str.replace() with slicing
def func9(word, n):
    return word.replace(word[:n], "")


# 10. map() and filter()
def func10(word, n):
    return "".join(map(lambda x: x[1], filter(lambda x: x[0] >= n, enumerate(word))))


# 11. Recursion-based removal
def func11(word, n):
    if n <= 0:
        return word
    return func11(word[1:], n - 1)


# 12. Using slicing with list conversion
def func12(word, n):
    return "".join(list(word)[n:])


# 13. Using slicing with tuple conversion
def func13(word, n):
    return "".join(tuple(word)[n:])


# 14. Using str.__getitem__ directly
def func14(word, n):
    return word.__getitem__(slice(n, None))


# 15. Regular expression (re.sub)
import re


def func15(word, n):
    pattern = f"^.{{{n}}}"
    return re.sub(pattern, "", word)


# 16. Using itertools.islice
from itertools import islice


def func16(word, n):
    return "".join(islice(word, n, None))


# 17. Using collections.deque
from collections import deque


def func17(word, n):
    d = deque(word)
    for _ in range(n):
        d.popleft()
    return "".join(d)


# 18. Using NumPy array slicing
import numpy as np


def func18(word, n):
    arr = np.array(list(word))
    return "".join(arr[n:])


# 19. memoryview on bytes
def func19(word, n):
    b = word.encode()
    mv = memoryview(b)
    return mv[n:].tobytes().decode()


# 20. bytearray slicing
def func20(word, n):
    ba = bytearray(word, "utf-8")
    return ba[n:].decode()


# 21. Using functools.reduce
from functools import reduce


def func21(word, n):
    return reduce(
        lambda acc, val: acc + val if val[0] >= n else acc, enumerate(word), ""
    )


# 22. Reversed slicing
def func22(word, n):
    return "".join(reversed(list(reversed(word))[n:]))


# 23. pandas Series
import pandas as pd


def func23(word, n):
    s = pd.Series(list(word))
    return "".join(s[n:].tolist())


# 24. Set slicing (sorted to preserve order)
def func24(word, n):
    return "".join(sorted(set(word[n:]), key=word.index))


# 25. array module slicing
import array


def func25(word, n):
    arr = array.array("u", word)
    return "".join(arr[n:])


# Main function to test all implementations
def main_func(label, func):
    print(label)
    print("Removing characters from a string")
    print(func("pynative", 4))  # Expected: 'tive'
    print(func("pynative", 2))  # Expected: 'native'
    print("-------------------------")


# Run all functions
main_func("1. String Slicing", func1)
main_func("2. Lambda Function", func2)
main_func("3. Negative Indexing", func3)
main_func("4. Loop-Based Removal", func4)
main_func("5. List Comprehension with str.join()", func5)
main_func("6. Generator Expression", func6)
main_func("7. filter with range", func7)
main_func("8. zip() and enumerate()", func8)
main_func("9. str.replace() with Slicing", func9)
main_func("10. map() and filter()", func10)
main_func("11. Recursion-Based Removal", func11)
main_func("12. List Slicing", func12)
main_func("13. Tuple Slicing", func13)
main_func("14. str.__getitem__ with slice", func14)
main_func("15. Regular Expression (re.sub)", func15)
main_func("16. Using itertools.islice", func16)
main_func("17. Using collections.deque", func17)
main_func("18. Using NumPy Array Slicing", func18)
main_func("19. memoryview on bytes", func19)
main_func("20. bytearray slicing", func20)
main_func("21. functools.reduce", func21)
main_func("22. Reversed Slicing", func22)
main_func("23. pandas Series", func23)
main_func("24. Set Slicing (sorted)", func24)
main_func("25. array module slicing", func25)
