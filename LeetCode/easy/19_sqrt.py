# https://leetcode.com/problems/sqrtx/

# Implement int sqrt(int x).

# Compute and return the square root of x, where x is guaranteed
# to be a non-negative integer.

# Since the return type is an integer, the decimal digits are
# truncated and only the integer part of the result is returned.

# Example 1:
# Input: 4
# Output: 2

# Example 2:
# Input: 8
# Output: 2

# Explanation: The square root of 8 is 2.82842..., and since
#              the decimal part is truncated, 2 is returned.


def mySqrt(x):

    return int(x**(1/2))


x = 8
# return 2
# print(mySqrt(x))

# binary search method of finding the sqrt root
# binary search if we recall, is O ( logn)
# were subtracting -1 from the highest left most position
# because even though we cancled 2 out, when we square 3,
# because y2 = x or |x = y2;


def sqrtHer(x):
    #  if x = 0, sqrt of 0 is 0
    # if x = 1, sqrt of 1 is 1
    if x < 2:
        return x

    left, right = 1,  x//2
    while left <= right:
        mid = left + (right-left) // 2
        #  or we can use if mid * mid > x
        if mid > x/mid:
            right = mid = -1
        else:
            left = mid + 1
    return left - 1


print(sqrtHer(x))
