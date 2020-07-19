# Binary search record and move on technique

def record(A, mid, output, target):

    if output == -1 or abs(A[mid] - target) < abs(A[output] - target):
        return mid
    
    return output

def binarySearch(A, target):

    if not A:
        return -1

    left = 0
    right = len(A) - 1
    output = 0

    while left <= right:
        mid = left + ((right - left) // 2)
        output = record(A, mid, output, target)

        
        if A[mid] > target:
            right = mid - 1
        elif A[mid] < target:
            left = mid + 1
        else:
            return A[output]
    
    return A[output]
    

target = 33
A = [10, 20, 30, 40, 50]
print(binarySearch(A, target))
    
