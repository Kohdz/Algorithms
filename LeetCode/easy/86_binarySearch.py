# https://leetcode.com/problems/binary-search/

def search(A, target):

    left = 0
    right = len(A) - 1

    while left <= right:
        
        mid = left + (right - left >> 1)
        
        if A[mid] == target:
            return mid
        
        if A[mid] < target:
            left = mid + 1 
        elif A[mid] > target:
            right = mid - 1
    return -1

target = 2
A = [-1,0,3,5,9,12]

print(search(A, target))