# https://leetcode.com/problems/next-permutation


def nextPermutationnums(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        
    #This is a math problem. From right to left, find the first one decreasing from the right. Num1
    #Then start from the right again, to find the first one larger than Num1
    #Swap Num1 and Num2, and then reverse all the following arrays after position of Num1
    #Time complexity, O(n), two scan
    #Spcae complexity, O(1), in place
        
        # Find the index where nums[i] < nums[i+1]
        i = j = len(nums)-1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        
        # list is sorted in decending order, return revered
        if i == 0:   # nums are in descending order
            nums.reverse()
            return 
       
        # find the index j where nums[j] is larger than nums[i] and swap
        k = i - 1    # find the last "ascending" position
        while nums[j] <= nums[k]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]  
        
        # sort the rest of the list in ascending order
        l, r = k+1, len(nums)-1  # reverse the second part
        
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l +=1 ; r -= 1

# EPI
def nextPermutation(perm):
    """
    Do not return anything, modify nums in-place instead.
    """

    inversion_point = len(perm) - 2

    while (inversion_point >= 0 and perm[inversion_point] >= perm[inversion_point + 1]):
        inversion_point -= 1

    if inversion_point == -1:
        return []  # perm is the last permutation

    for i in reversed(range(inversion_point + 1, len(perm))):
        if perm[i] > perm[inversion_point]:
            perm[inversion_point], perm[i] = perm[i], perm[inversion_point]
            break

    perm[inversion_point + 1:] = reversed(perm[inversion_point + 1:])
    return perm


perm = [1, 2, 3]  # 1, 3, 2
print(nextPermutation(perm))
