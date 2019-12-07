# Given a non-negative int n, return the count of the occurrences of 7 as a digit,
# so for example 717 yields 2. (no loops). Note that mod (%) by 10 yields the rightmost
# digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).


# count7(717) → 2
# count7(7) → 1
# count7(123) → 0


def count7(n):
    seven = 0
    if n == 0:
        return 0

    mod = n % 10
    if mod == 7:
        seven += 1

    return seven + count7(n // 10)


def count7II(n):

    if n == 0:
        return 0

    return (1 if n % 10 == 7 else 0) + count7II(n // 10)


nums = 717
nums2 = 7
nums3 = 123

print(count7II(nums3))
