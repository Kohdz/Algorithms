# https://leetcode.com/problems/kth-missing-positive-number/

def findKthPositive(arr, k):

    prev = 0
    count = 0
    for curr in arr:
        count += curr-prev-1
        if count >= k:
            return curr-(count-k+1)
        prev = curr 
    return arr[-1] + (k-count) 

def findKthPositiveBinSearch(A, k):

    left, right = 0, len(A)
    while left < right:
        mid = (left + right + 1) // 2
        if mid:
            if A[mid - 1] - mid < k:
                left = mid
            else:
                right = mid - 1
        else:
            if 0 - mid < k:
                left = mid
            else:
                right = mid -1

    return left + k

k = 5
arr = [2,3,4,7,11]
# Output: 9

print(findKthPositive(arr, k))