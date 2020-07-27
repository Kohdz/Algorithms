# https://leetcode.com/problems/peak-index-in-a-mountain-array


# Time  O(N)
# Space O(1)
def peakIndexInMountainArray(A):
    for i in range(len(A)):
        if A[i] > A[i+1]:
            return i

# Binary search approach
# we binary search over this array of comparsions
# to find the largest index of i such that A[i] < A[i + 1]

# Time  O( logn)
# Space O (1)
def peakIndexInMountainArrayBinarySearch(A):

    left, right = 0, len(A) - 1

    while left < right:
        mid = left + (right - left >> 1)

        if A[mid] < A[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left