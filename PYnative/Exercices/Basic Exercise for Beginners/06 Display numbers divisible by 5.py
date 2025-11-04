"""
Exercise 6: Display numbers divisible by 5
Write a Python code to display numbers from a list divisible by 5.
"""


def func1(nums, num):
    result = []
    for i in nums:
        if i % num == 0:
            result.append(i)
    return result


def func2(nums, num):
    return (val for i, val in enumerate(nums) if i % num == 0)


# Main function to test all implementations
def main_func(label, func):
    nums = [10, 20, 33, 46, 55]
    num = 5
    print(label)
    print(f"Given list is {nums}")
    print(f"Divisible by {num}")
    print(func(nums, num))
    print("---------------------------")


main_func("1. ", func1)
main_func("2. ", func2)
