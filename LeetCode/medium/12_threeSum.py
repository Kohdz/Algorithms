
def threeSumTarget(nums, target):
    nums.sort()

    for i in range(len(nums)-2):

        partial_target = target - nums[i]
        j = i + 1
        k = len(nums) - 1

        while j < k:

            partial_sum = nums[j] + nums[k]

            if partial_sum == partial_target:
                return (nums[i], nums[j], nums[k])
            elif partial_sum > partial_target:
                k -= 1
            else:
                j += 1
        return None


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
