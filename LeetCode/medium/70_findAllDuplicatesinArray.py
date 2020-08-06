# https://leetcode.com/problems/find-all-duplicates-in-an-array/

# Time O(n) | Space O(1)

def findDuplicates(nums):

    result = []
    for n in nums:
        n = abs(n)
        if nums[n - 1] > 0:
            nums[n - 1] *= -1
        else:
            result.append(n)
    return result

nums =[4,3,2,7,8,2,3,1]
print(findDuplicates(nums))