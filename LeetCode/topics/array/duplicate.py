# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array,
# and it should return false if every element is distinct.

# Example 1:
# Input: [1,2,3,1]
# Output: true

# Example 2:
# Input: [1,2,3,4]
# Output: false

# Example 3:
# Input: [1,1,1,3,3,4,3,2,4,2]
# Output: true


def containsDuplicate(nums):
    dups = False
    dict = {}

    for i in nums:
        print(i)
        if i not in dict:
            dict[i] = i
        else:
            dups = True

    return dups


nums = [1, 2, 3, 1]
nums2 = [1, 2, 3, 4]
nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

print("Should be True: ", containsDuplicate(nums))
print("Should be False: ", containsDuplicate(nums2))
print("Should be True: ", containsDuplicate(nums3))


def containsDuplicate2(nums):
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i+1]:
            return True
    return False