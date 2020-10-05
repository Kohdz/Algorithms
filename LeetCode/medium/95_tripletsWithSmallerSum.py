'''Given an array arr of unsorted numbers and a target sum, count all triplets in it such that
arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices.
Write a function to return the count of such triplets.

Example 1
Input: [-1, 0, 2, 3], target=3 
Output: 2
Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]

Exaple 2
Input: [-1, 4, 2, 1, 3], target=5 
Output: 4
Explanation: There are four triplets whose sum is less than the target: 
   [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]'''




def tripletsSmallerSum(arr, target):

    arr.sort()
    output = 0

    for i in range(len(arr)-2):
        left = i + 1
        right = len(arr) - 1

        while left < right:

            _sum = arr[i] + arr[left] + arr[right]

            # found the triplet
            if _sum < target:

                # since arr[right] >= arr[left], therefore we can replace arr[right] by any number
                # between left and right to get a sum less that the target  
                output += right - left
                
                # return list of nums an dnot count
                # for j in range(right, left - 1):
                #     output.append([arr[i], arr[left], arr[right]])
                
                left += 1
            else:
                # we need a pair with a smaller sum
                right -= 1

    return output


target1 = 3
arr1 = [-1, 0, 2, 3]

target2 = 5
arr2 = [-1, 4, 2, 1, 3]

print(tripletsSmallerSum(arr1, target1))
print(tripletsSmallerSum(arr2, target2))