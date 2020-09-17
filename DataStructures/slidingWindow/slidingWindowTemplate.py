# https://leetcode.com/discuss/general-discussion/657507/Sliding-Window-for-Beginners-Problems-or-Template-or-Sample-Solutions

def longestOnes(A, k):

    count = 0
    i = 0 
    j = 0
    res = 0

    for i in range(A):
        # have some hashmap or counter
        if A[i] == 0:
            count += 1 

        # loop inside for loop to reduce the window size based on constraints
        while count > k and j < len(A):
            count -= 1
            j += 1

        # get the maximum value of the window which satisfies the constraint
        res = max(res, i - j  + 1)

        return res