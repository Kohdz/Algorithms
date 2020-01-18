# Task: Find the missing term in an Arithmetic Progression – An Arithmetic Progression is defined as one in which there is a constant difference between 
# the consecutive terms of a given series of numbers. You are provided with consecutive elements of an Arithmetic Progression. There is however one hitch: 
# Exactly one term from the original series is missing from the set of numbers which have been given to you. The rest of the given series is the same as the 
# original AP. Find the missing term.

# Input Format: The first line contains an Integer N, which is the number of terms which will be provided as input. This is followed by N consecutive Integers,
#  with a space between each pair of integers. All of these are on one line, and they are in AP (other than the point where an integer is missing).

# Output Format: One Number which is the missing integer from the series.

# Sample Input: 
# 1 3 5 9 11

# Sample Output: 
# 7

# Explanation: You are provided with 5 integers. As you can can observe, they have been picked from a series, in which the starting term is 1 and the common difference is 2.
#  The only abberration, i.e. the missing term (7), occurs between 5 and 9. This is the missing element which you need to find.

# Constraints: 3 <= N <= 2500. All integers in the series will lie in the range [-10^6,+10^6].


# Complexity O(n^2) time
N = int(input("Number of Items: "))
s = input("Consecutive Integers with a space: ")
arr1 = list(map(int, s.split()))

def ArithmeticProgression(n, arr1):
    diff = int((arr1[n-1] - arr1[0]) / n)

    miss = 0
    j = 1
    for i in range(n-1):
        if arr1[j] - arr1[j-1]  != diff:
            miss = arr1[j]
        j+= 1
    
    miss_updated = miss - diff
    return miss_updated

print(ArithmeticProgression(N, arr1))



# arr1 = [1,3,5,9,11]
# n = len(arr1)

# Complexity O(log n)
def ArithmeticProgressionRecursion(n, arr1):
    return 0






# Complexity O(n) time
# def ArithmeticProgression(n, arr1):
#     diff = int((arr1[len(arr1)-1] - arr1[0]) / len(arr1))
#     arr_len = len(arr1)
#     miss = 0
#     j = 1
#     for i in range(len(arr1)-1):
#         if arr1[j] - arr1[j-1]  != diff:
#             miss = arr1[j]
#         j+= 1
    
#     miss_updated = miss - diff
#     return miss_updated

# print(AP(n, arr1))

# Complexity O(log n)
# def ArithmeticProgressionRecursion(n, arr1):
#     return 0
