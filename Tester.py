nums = [2, 2, 3, 1]

numSet = set(nums)
numsList = list(numSet)
numsSorted = sorted(numsList)


numComp = sorted(list(set(nums)))


print("nums: ", nums)
print("numSet: ", numSet)
print("numsList: ", numsList)
print("numsSorted: ", numsSorted)
print("numComp: ", numComp)
