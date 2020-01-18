
# Given n of 1 or more, return the factorial of n, which is n * (n-1) * (n-2) ...
# 1. Compute the result recursively (without loops).


# factorial(1) → 1
# factorial(2) → 2
# factorial(3) → 6


def factorial(n):

    if n == 1:
        return 1

    return n * factorial(n-1)


n = 1
n1 = 2
n2 = 2
print(factorial(n))
print(factorial(n1))
print(factorial(n2))
