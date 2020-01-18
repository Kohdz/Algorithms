def reverse(x):
    result, x_remaining = 0, abs(x)

    while x_remaining:
        result = result * 10 + x_remaining % 10
        x_remaining //= 10

    return -result if x < 0 else result


x = 71
print(bin(71))
print(reverse(x))
