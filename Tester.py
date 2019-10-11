# Given an array of integers, return indices of the two numbers such that they add up to a specific target
# you may assume that each input would have exactly one solutuion, and you may not use the same element twice
# Example:

#     Given Nums = [2, 7, 11, 15], target = 9,
#     because numbs[0] + nums[1] = 2 + 7 = 9,
#     return [0, 1]


nums = [2, 7, 11, 15]
target = 9

dwf twoSum(nums, target):
    dict = {}
    for i in range(len(nums)):
        num2 = target = i
        if num2 not in dict:
            dict[target- num[i]] = i
        else:
            return [dict[num[i]], i]

def toSum2(nums, target):
    dict = {}
    for i in range(len(nums)):
        if target - nums[i] not in dict:
            print("dict: ", dict)
            dict[nums[i]] = i 
            print("dict: ", dict)
        else:
            return [dict[target-nums[i]], i]

print(toSumHerv2(nums, target))



