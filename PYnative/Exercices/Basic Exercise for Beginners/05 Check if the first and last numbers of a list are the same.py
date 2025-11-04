'''
Exercise 5: Check if the first and last numbers of a list are the same
Write a code to return True if the list's first and last numbers are the same. If the numbers are different, retun False'''


def func1(nums):
    return nums[0] == nums[-1]


def func2(nums):
    if nums[0] == nums[-1]:
        return True
    return False


def main_func(func):
    nums1 = [10, 20, 30, 10]
    nums2 = [10, 20, 30, 40]
    print(func(nums1))
    print(func(nums2))


main_func(func1)
main_func(func2)

