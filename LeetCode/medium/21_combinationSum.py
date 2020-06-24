# https://leetcode.com/problems/combination-sum/

def combinationSum(candidates, target):

    def backtrack(candidates, target, res, ans, inx):
        
        if sum(ans) > target:
            return

        if sum(ans) == target:
            res.append(ans[:])
            return

        for i in range(inx, len(candidates)):
            ans.append(candidates[i])
            backtrack(candidates, target, res, ans, i)
            ans.pop()



    res = []
    candidates.sort()
    backtrack(candidates, target, res, [], 0)
    return res

candidates = [2,3,6,7]
target = 7

print(combinationSum(candidates, target))

