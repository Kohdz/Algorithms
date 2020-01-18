# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

# Example 1:
# Input: [3,0,1]
# Output: 2

# Example 2:
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8


def missingNumber(nums):
    nums.sort()

    # Ensure that n is at the last index
    if nums[-1] != len(nums):
        return len(nums)
    # Ensure that 0 is at the first index
    elif nums[0] != 0:
        return 0

    # If we get here, then the missing number is on the range (0, n)
    for i in range(1, len(nums)):
        expected_num = nums[i-1] + 1
        if nums[i] != expected_num:
            return expected_num

# print(missingNumber(nums))


def missingNumber2(nums):
    num_set = set(nums)
    print(num_set)
    n = len(nums) + 1
    for number in range(n):
        if number not in num_set:
            return number


nums = [3, 0, 1]
nums2 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
nums3 = [0, 1]

print(missingNumber(nums))