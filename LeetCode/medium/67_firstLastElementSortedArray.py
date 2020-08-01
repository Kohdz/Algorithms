# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

# Time O (log(n)) | Space O (1)

def searchRange(nums, target):

    if len(nums) == 0:
        return [-1, -1]

    left, right = 0, len(nums)

    while left < right:

        mid = left + (right - left >> 1)

        if nums[mid] == target:

            left, right = mid, mid

            while left - 1 >= 0 and nums[left - 1] == target:
                left -= 1
            
            while right + 1 < len(nums) and nums[right + 1] == target:
                right += 1

            return [left, right]

        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    return [-1, -1]


target = 8
nums = nums = [5,7,7,8,8,10]
# output [3, 4]
print(searchRange(nums, target))