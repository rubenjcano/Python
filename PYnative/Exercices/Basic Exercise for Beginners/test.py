# Shared logic
def compute_values(num1: int, num2: int) -> tuple[int, int]:
    product = num1 * num2
    suma = num1 + num2
    return product, suma

# 1. Original
def func1(num1, num2):
    product, suma = compute_values(num1, num2)
    return f"The result is {product}" if product <= var else f"The result is {suma}"

# 2. Ternary Operator
def func2(num1, num2):
    product, suma = compute_values(num1, num2)
    return f"The result is {product}" if product <= var else f"The result is {suma}"

# 3. Early Return
def func3(num1, num2):
    product, suma = compute_values(num1, num2)
    if product <= var:
        return f"The result is {product}"
    return f"The result is {suma}"

# 4. Lambda Function
func4 = lambda num1, num2: (
    f"The result is {num1 * num2}" if num1 * num2 <= var else f"The result is {num1 + num2}"
)
# Note: Lambdas can't use external helper unless you wrap them.

# 5. Class-Based Approach
class NumberProcessor:
    def __init__(self, num1: int, num2: int):
        self.num1 = num1
        self.num2 = num2

    def processor(self) -> str:
        product, suma = compute_values(self.num1, self.num2)
        return f"The result is {product}" if product <= var else f"The result is {suma}"

def func5(num1: int, num2: int) -> str:
    return NumberProcessor(num1, num2).processor()

# 6. Pattern Matching
def func6(num1, num2):
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
    print("-------------------")

# Threshold
var = 1000

# Run all versions
versions(func1, "1. Original")
versions(func2, "2. Ternary Operator")
versions(func3, "3. Early Return")
versions(func4, "4. Lambda Function")
versions(func5, "5. Class-Based Approach")
versions(func6, "6. Pattern Matching")