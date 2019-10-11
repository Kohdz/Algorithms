# Given an array of integers, return indices of the two numbers such that they add up to a specific target
# you may assume that each input would have exactly one solutuion, and you may not use the same element twice
# Example:

#     Given Nums = [2, 7, 11, 15], target = 9,
#     because numbs[0] + nums[1] = 2 + 7 = 9,
#     return [0, 1]


def twoSum(num, target):

    fin_list = []
    counter = 1
    for i in range(len(nums)):
        for j in range(len(nums)):
            if num[i] + num[j] == target:
                if i & j not in fin_list:
                    fin_list.append(i)
                    fin_list.append(j)

    return fin_list

nums = [2, 7, 11, 15]
target = 9
# print(twoSum(nums, target))

def twoSumHer(nums, target):
    for i in nums:
        j = target - i
        start_index = nums.index(i)
        next_index = start_index + 1
        temp_nums = nums[next_index:]
        if j in temp_nums:
            return(nums.index(i), next_index + temp_nums.index(j))

print(twoSumHer(nums, target))

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


