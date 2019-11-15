# https://leetcode.com/problems/single-number/

# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

# Note:

# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Example 1:
# Input: [2,2,1]
# Output: 1

# Example 2:
# Input: [4,1,2,1,2]
# Output: 4


def singleNumber(nums):

    dict = {}

    for i in range(len(nums)):
        if nums[i] not in dict:
            dict[nums[i]] = 1
        else:
            dict[nums[i]] += 1

    for key, value in dict.items():
        if value == 1:
            return key


nums = [2, 2, 1]
nums2 = [4, 1, 2, 1, 2]
# should return 4
print(singleNumber(nums2))


def singleNumberBit(nums):

    ans = 0

    # when we XOR, we are changing 0 to that XOR
    # but when we XOR again, meaning, if a number repreats
    # then  its XOR will simply reverse it back to 0
    #  the only time it will not repeat is if  there is only 1 value
    for num in nums:
        ans ^= num

    return ans


def singleNumberHash(nums):
    hash_table = {}

    for i in nums:
        try:
            hash_table.pop(i)
        except:
            hash_table[i] = 1

    return hash_table.popitem()[0]
