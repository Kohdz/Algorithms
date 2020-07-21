# https://leetcode.com/problems/find-lucky-integer-in-an-array/


def findLucky(arr):
    dict = {}
    
    for num in arr:
        
        if num not in dict:
            dict[num] = 1
        else:
            dict[num] += 1
            
    output = float('-inf')
    for key, value in dict.items():
        
   
        if key == value and key > output:
            output = key
            
    return max(output, -1)


arr = [2,2,3,4]
print(findLucky(arr))