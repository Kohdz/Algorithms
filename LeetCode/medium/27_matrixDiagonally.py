# https://leetcode.com/problems/sort-the-matrix-diagonally/
import collections
from heapq import heappush, heappop

def diagonalSort(matrix):
    
    #create a dictionary
    hash_map = collections.defaultdict(list)

    #traverse the matrix.
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            
            #now we take out the difference of i'th and j'th indices 
            #  (dont take the absolute value, coz we need to   use the 
            # diff as unique keys in our dictionary representing every Diagonal).
            diff = i-j
            
            #we set the default value of the dictionary to a List type, so that we 
            # can store all the values of a Diagonal in the same list under the 
            # same Key(that is the difference between the i'th  & j'th index).
            hash_map.setdefault(diff,[]).append(matrix[i][j])

    #now we traverse the dictionary and sort the value(list)
    # stored in every key which represented the values of a diagonal.
    for i in hash_map:
        hash_map[i].sort()

    #now we traverse the matrix again, this time to store the
    # values in sorted order from our dictionary.    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
                
            #we take out the differences between i'th and
            # j'th index again to match it to the keys of the dictionary.
            diff = i-j
                
            #now we store the first value of the key to the
            # current matrix block(coz we have sorted it already).
            matrix[i][j] = hash_map[diff][0]
                
            #now we remove the first value form the list of key we
            # used, so as to add the remaining vlaues in the preceeding loops.
            hash_map[diff].pop(0)

    #final diagonally sorted matrix returned
    return matrix

def diagonalSortHeap(matrix):
    d = collections.defaultdict(list)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            heappush(d[i-j], matrix[i][j])
        
    res = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            res[i][j] = heappop(d[i-j])
    return res

matrix = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]

# Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
print(diagonalSort(matrix))