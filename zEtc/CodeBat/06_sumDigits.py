
# Given a non-negative int n, return the sum of its digits recursively (no loops).
# Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) by 10
# removes the rightmost digit (126 / 10 is 12).


# sumDigits(126) → 9
# sumDigits(49) → 13
# sumDigits(12) → 3

def sumDigitsIterative(n):
    a = n

    sums = 0
    while n > 0:
        mod = n % 10
        sums += mod
        n = n // 10

    return sums


def sumDigitsRec(n):
    num = 0
    if n == 0:
        return 0

    num = n % 10

    return num + sumDigitsRec(n//10)


def sumDigitsRecII(n):
    if n == 0:
        return 0

    return n % 10 + sumDigitsRecII(n // 10)


nums = 126  # 9
nums2 = 49  # 13
nums3 = 12  # 3

print(sumDigitsRec(nums))
print(sumDigitsRec(nums2))
print(sumDigitsRec(nums3))
