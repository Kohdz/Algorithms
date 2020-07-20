# https://leetcode.com/problems/find-k-closest-elements

# Assume we are taking A[i] ~ A[i + k -1].
# We can binary research i
# We compare the distance between x - A[mid] and A[mid + k] - x

# Assume A[mid] ~ A[mid + k] is sliding window

# If x - A[mid] > A[mid + k] - x,
# it means A[mid + 1] ~ A[mid + k] is better than A[mid] ~ A[mid + k - 1],
# and we have mid smaller than the right i.
# So assign left = mid + 1.

def findClosestElements(A, k, target):


    left, right = 0, len(A) - k
    while left < right:
        mid = left + (right - left)//2
        if target - A[mid] > A[mid + k] - target:
            left = mid + 1
        else:
            right = mid
    return A[left:left + k]

k = 4
target = 3
A = [1,2,3,4,5]
# Output: [1,2,3,4]
print(findClosestElements(A, k, target))

