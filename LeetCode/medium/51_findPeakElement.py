# https://leetcode.com/problems/find-peak-element/

def findPeakElement(A):
    
    if len(A) == 1:
        return 0
    left, right = 0, len(A) - 1
    while left < right:
        mid = (left + right) // 2
        if A[mid] > A[mid+1]:
            right = mid
        else:
            left = mid + 1
    return left


A = [1,2,3,1]
# Output: 2

print(findPeakElement(A))