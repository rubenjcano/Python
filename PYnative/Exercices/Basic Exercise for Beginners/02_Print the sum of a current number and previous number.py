# 1. Original
def func1(num: int) -> str:
    print(f"Printing current and previous number sum in a range({num})")
    previous_num = 0
    for current_num in range(num):
        print(
            f"Current Number {current_num} Previous Number {previous_num} Sum: {current_num + previous_num}"
        )
        current_num += 1
        previous_num = current_num - 1


# 2. Improved version
def func2(num: int) -> str:
    print(f"Printing current and previous number sum in a range({num})")
    previous_num = 0
    for current_num in range(num):
        sum_val = current_num + previous_num
        print(
            f"Current Number {current_num} Previous Number {previous_num} Sum: {sum_val}"
        )
        previous_num = current_num


# 3. Enumerate with a list
def func3(num: int):
    print(f"Printing current and previous number sum in a range({num})")
    nums = list(range(num))
    previous_num = 0
    for i, current_num in enumerate(nums):
        """
        In Python, enumerate() is a built-in function that allows you to loop over an iterable (like a list or range)
        and get both the index and the value at the same time.
        i and current_num are the same
        Since I am not using the i (the index) I could use "for current_num in nums"
        Syntax:
        for index, value in enumerate(iterable):
            use index and value
        """
        sum_val = current_num + previous_num
        print(
            f"Current Number {current_num} Previous Number {previous_num} Sum: {sum_val}"
        )
        previous_num = current_num


# 4. Zip to pair current and previous nums
def func4(num: int):
    print(f"Printing current and previous number sum in a range({num})")
    nums = list(range(num))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    previous_nums = [0] + nums[:-1]  # [0, 0, 1, 2, 3, 4, 5, 6, 7, 8]
    for current_num, previous_num in zip(
        nums, previous_nums
    ):  # [(0, 0), (1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7), (9, 8)]
        sum_val = current_num + previous_num
        print(
            f"Current Number {current_num} Previous Number {previous_num} Sum: {sum_val}"
        )


# 5. Recursion
def func5(num: int, current_num: int = 0, previous_num: int = 0):
    sum_val = current_num + previous_num
    if current_num >= num:
        return
    print(f"Current Number {current_num} Previous Number {previous_num} Sum: {sum_val}")
    func5(num, current_num + 1, current_num)


# 6
def func6(num: int, previous_num: int = 0):
    for current_num in range(num):
        sum_val = current_num + previous_num
        print(
            f"Current Number {current_num} Previous Number {previous_num} Sum: {sum_val}"
        )
        previous_num = current_num


num = 10


# Versions
def versions(func, label):
    print(label)
    func(num)
    print("---------------------------------------")


versions(func1, "1. Original")
versions(func2, "2. Improved version")
versions(func3, "3. Enumerate with a list")
versions(func4, "4. Zip to pair current and previous nums")
versions(func5, "5. Recursion")
versions(func6, "6")
