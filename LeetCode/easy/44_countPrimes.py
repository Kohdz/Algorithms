# Count the number of prime numbers less than a non-negative number, n.


# Example:
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

def countPrimes(n):

    if n <= 1:
        return 0

    nums = [None] * n
    nums[0] = False
    nums[1] = False

    for i in range(n):
        if nums[i] == None:
            nums[i] = True

            for j in range(i + i, n, i):
                nums[j] = False

    return sum(nums)


n = 10
print(countPrimes(n))
