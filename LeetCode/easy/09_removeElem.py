# https://leetcode.com/problems/remove-element/
# Given an array nums and a value val, remove all instances of that value in-place and return the new length.

# Do not allocate extra space for another array, you must do this by modifying the
# input array in-place with O(1) extra memory.

# The order of elements can be changed. It doesn't matter
#  what you leave beyond the new length.

# Example 1:
# Given nums = [3,2,2,3], val = 3,
# Your function should return length = 2, with the first two elements of nums being 2.
# It doesn't matter what you leave beyond the returned length.

# Example 2:
# Given nums = [0,1,2,2,3,0,4,2], val = 2,
# Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.
# Note that the order of those five elements can be arbitrary.
# It doesn't matter what values are set beyond the returned length.


nums = [3, 2, 2, 3]
val = 3

nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
val2 = 2


def removeElement(nums, val):

    stack = []
    for i in range(len(nums)):
        if nums[i] == val:
            stack.append(nums[i])

    while stack != []:
        pop = stack.pop()
        nums.remove(pop)
    return nums


# print("Expected: [0,1,4,0,3]: ", removeElement(nums, val))


def removeElementHer(nums, val):

    i, last = 0, len(nums) - 1

    while i <= last:
        if nums[i] == val:
            nums[i], nums[last] = nums[last], nums[i]
            last -= 1
        else:
            i += 1

    return last+1


print(removeElementHer(nums, val))

# why does nums change
