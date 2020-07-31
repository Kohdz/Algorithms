# https://leetcode.com/problems/3sum/


# For time complexity
# Sorting takes `O(NlogN)`
# Now, we need to think as if the `nums` is really really big
# We iterate through the `nums` once, and each time we iterate the whole array again by a while loop
# So it is `O(NlogN+N^2)~=O(N^2)`

# For space complexity
# We didn't use extra space except the `res`
# Since we may store the whole 'nums' in it
# So it is `O(N)`
# `N` is the length of `nums`



def threeSum(nums):

    res = []
    nums.sort()
    if len(nums) < 3:
        return res

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == 0:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
            elif s < 0:
                l += 1
            else:
                r -= 1
    return res


nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
