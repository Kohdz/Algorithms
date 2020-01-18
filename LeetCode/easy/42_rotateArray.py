# Given an array, rotate the array to the right by k steps, where k is non-negative.

# Example 1:
# Input: [1,2,3,4,5,6,7] and k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Example 2:
# Input: [-1,-100,3,99] and k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]


def rotate(nums, k):

    numLen = len(nums)
    numsRotated = []
    for i in reversed(range(numLen-k, numLen)):
        numsRotated.insert(0, nums[i])

    newNums = numsRotated + nums
    return newNums[0:numLen]


nums = [-1, -100, 3, 99]
k = 2
# output: [5,6,7,1,2,3,4]
print(rotate(nums, k))


def rotateHer(nums, k):

    k = k % len(nums)

    nums[:k], nums[k:] = nums[len(nums) - k:], nums[: len(nums)-k]


# time (n * k) all nums are shifted by one step (n) k times (k)
#  O (1) space
def rotateBrute(nums, k):
    temp = 0
    previous = 0

    for i in range(k):
        previous = nums[len(nums)-1]
        for j in range(len(nums)):
            temp = nums[j]
            nums[j] = previous
            previous = temp


def rotateSlicing(nums, k):

    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]


# time (n) | space (1)
def listReversal(nums, start, end):
    # Original List                   : 1 2 3 4 5 6 7
    # After reversing all numbers     : 7 6 5 4 3 2 1
    # After reversing first k numbers : 5 6 7 4 3 2 1
    # After revering last n-k numbers : 5 6 7 1 2 3 4 --> Result

    while (start < end):
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1


def listRotate(nums, k):
    k = k % len(nums)
    listReversal(nums, 0, len(nums)-1)
    listReversal(nums, 0, k-1)
    listReversal(nums, k, len(nums)-1)
