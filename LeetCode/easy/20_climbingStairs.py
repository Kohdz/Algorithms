# https://leetcode.com/problems/climbing-stairs/

# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Note: Given n will be a positive integer.

# Example 1:
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step


# problem with this method is that it is wasteful
# for example in n = 3, you have to recompute n =2 and n = 1
def climbStairs(n):
    if n == 0 or n == 1:
        return 1
    else:
        return climbStairs(n-1) + climbStairs(n-2)

    return 0


n = 2  # output should be 2
n = 3  # output should be 3
print(climbStairs(n))

# thus you use whats called dyamic programmng
# since we know that this is the fibbinoic sequence
# we can use a dictionary to cache data


# def num_ways_bottom_up(n):
#     if n == 0 or n == 1:
#         return 1

#     # integer array of len(n+1)
#     nums = new int[n+1]

#     # we can assgin nums[0] and nums[1]
#     # becasue they are our base case
#     nums[0], nums[1] = 1, 1

#     for i in range(2, len(n)):
#         nums[i] = nums[i-1] nums[i-2]

#     return nums[n]


def climbingStairs(n):

    prev, current = 0, 1
    for i in range(n):
        prev, current = current, prev + current
    return current
