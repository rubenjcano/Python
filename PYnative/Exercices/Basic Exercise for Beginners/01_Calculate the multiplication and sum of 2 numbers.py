# Shared logic
def compute_values(num1: int, num2: int) -> tuple[int, int]:
    product = num1 * num2
    suma = num1 + num2
    return product, suma


# 1. Original
def multiplication_or_sum_1(num1: int, num2: int) -> str:
    product, suma = compute_values(num1, num2)
    if product <= var:
        return f"The result is {product}"
    return f"The result is {suma}"


# 2. Ternary Operator
def multiplication_or_sum_2(num1: int, num2: int) -> str:
    product, suma = compute_values(num1, num2)
    return f"The result is {product}" if product <= var else f"The result is {suma}"


# 3. Early Return
def multiplication_or_sum_3(num1: int, num2: int) -> str:
    product, suma = compute_values(num1, num2)
    if product <= var:
        return f"The result is {product}"
    return f"The result is {suma}"


# 4. Lambda Function
multiplication_or_sum_4 = lambda num1, num2: (
    f"The result is {num1 * num2}"
    if num1 * num2 <= var
    else f"The result is {num1 + num2}"
)


# 5. Class-Based Approach
class NumberProcessor:
    def __init__(self, num1: int, num2: int):
        self.num1 = num1
        self.num2 = num2

    def process(self) -> str:
        product, suma = compute_values(self.num1, self.num2)
        if product <= var:
            return f"The result is {product}"
        return f"The result is {suma}"


def multiplication_or_sum_5(num1: int, num2: int) -> str:
    return NumberProcessor(num1, num2).process()


# 6. Pattern Matching (Python 3.10+)
def multiplication_or_sum_6(num1: int, num2: int) -> str:
    product, suma = compute_values(num1, num2)
    match product:
        case i if i <= var:
            return f"The result is {i}"
        case _:
            return f"The result is {suma}"


# Test Runner
def versions(func, label):
    print(label)
    print(func(20, 30))  # product = 600
    print(func(40, 30))  # product = 1200
    print("-------------------------------------")


var = 1000

versions(multiplication_or_sum_1, "1. Original")
versions(multiplication_or_sum_2, "2. Ternary Operator")
versions(multiplication_or_sum_3, "3. Early Return")
versions(multiplication_or_sum_4, "4. Lambda Function")
versions(multiplication_or_sum_5, "5. Class-Based Approach")
versions(multiplication_or_sum_6, "6. Pattern Matching")
