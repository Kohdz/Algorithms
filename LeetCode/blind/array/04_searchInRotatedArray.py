# https://leetcode.com/problems/search-in-rotated-sorted-array/

def search(A, target):
        

    left, right = 0, len(A) - 1
    
    while left <= right:
        
        mid = left + (right- left) //2
        
        if A[mid] == target:
            return mid

        if (target < A[0] and not target < A[mid] < A[0] or
                target >= A[0] and A[0] <= A[mid] < target):
            left = mid + 1
        else:
            right = mid - 1
    return -1
    

nums = [4,5,6,7,0,1,2]
target = 0

print(search(nums, target))