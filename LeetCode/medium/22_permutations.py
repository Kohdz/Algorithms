# https://leetcode.com/problems/permutations/


nums = [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]



def permuteI(nums):
    
    def dfs(nums, level, path, res):

        if level == 0:
            res.append(path)
            return
        
        for i in range(0, len(nums)):
            if nums[i] not in path:
                dfs(nums, level-1, path + [nums[i]], res)

    res = []
    dfs(nums, len(nums), [], res)
    return res


def permuteII(nums):
    
    def helper(arr, permutations_list, permutations_set):

        if len(permutations_set) == len(arr):

            res.append(permutations_list)
            return

        for i in range(0, len(arr), 1):
            if arr[i] not in permutations_set:
                permutations_set.add(arr[i])
                helper(arr, permutations_list + [arr[i]], permutations_set)
                permutations_set.remove(arr[i]) 

    res = []
    helper(nums, [], set())
    return res


# print(permuteI(nums))
print(permuteII(nums))