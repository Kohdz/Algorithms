# Multiply two Arbitrary-Precision Integer

# → certain applications require arbitrary precision arithmetic
# → one way to do this is to use arrays to represent integers
# 	→ e.g. with one digit per array entry
# → with the most significant digit appearing first and a negative leading digit denoting a 	negative integer

# time O (nm)l there are m partial products, with at most n+1 digits
# we perform O (1) operations on each digit in each partial product


def multiply(num1, num2):
    sign = -1 if (num1[0] < 0) + (num2[0] < 0) else 1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    result = [0] * (len(num1) + len(num2))

    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i + j + 1] += num1[i] * num2[j]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10

    # remove the leading zeros
    result = result[next((i for i, x in enumerate(result)
                          if x != 0), len(result)):] or [0]

    return [sign * result[0]] + result[1:]


num1 = [1, 9, 3, 7, 0, 7, 7, 2, 1]
num2 = [-7, 6, 1, 8, 3, 8, 2, 5, 7, 2, 8, 7]
# output: [-1, 4, 7, 5, 7, 3, 9, 5, 2, 5, 7, 9, 6, 7, 6, 4, 1, 2, 9, 2, 7]
print(multiply(num1, num2))
