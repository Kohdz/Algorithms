# https://leetcode.com/problems/sort-colors/


def sortColors(A):
    """
    Do not return anything, modify nums in-place instead.
    """
    
    pivot = 1
    smaller, equal, larger = 0, 0, len(A)
    
    while equal < larger:
        
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] == pivot:
            equal += 1
        else:
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]


A = [2,0,2,1,1,0]
print(sortColors(A))