# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

def kWeakestRowsArray(mat, k):
    
    strenghts, output = [], []
    
    for i in range(len(mat)):
        strenghts.append([mat[i].count(1), i])
        
    strenghts.sort()
    
    for i in range(k):
        
        output.append(strenghts[i][1])
        
    return output

def kWeakestRowsHashMap(mat, k):
    hash_map = {}
    for i, row in enumerate(mat):
        hash_map[i] = sum(row)

    	# 	# Sort the hashmap by values
        # hashmap = {k:v for k, v in sorted(hashmap.items(), key=lambda x:x[1])}
        # output = list(hashmap.keys())

    return sorted(hash_map, key = hash_map.get)[:k] 



from heapq import heappushpop, heappush, heappop



def kWeakestRowsHeap(mat, k):
    # Time O (n*m + n log k) | Space O (k)


    # size O(k)
    heap = []

    # iterate over the wros in O(m)
    for index, row in enumerate(mat):
        soldier_counts = soldier_count(row)

        # Push values to the heap in O (log k)
          
        if len(heap) == k:
            heappushpop(heap, (-soldier_counts, -index))
        else:
            heappush(heap, (-soldier_counts, -index))

    # size O (k)
    weakest_rows = []

    # Push the heap values into our result list in O (k log k)
    while heap:
        weakest_rows.append(-heappop(heap)[1])

    # Return the results in reversed order

def soldier_count(row):

    left, right = 0, len(row) - 1

    while left < right:
        mid = left + (right - left >> 1)

        if not row[mid]:
            right = mid - 1
        else:
            left = mid

    # we need to return a count and not an index
    # therefore we need to increase the result by one if solders have been found
    if row[0]:
        left += 1

    return left


k = 3
mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 

# Output: [2,0,3]

# print(kWeakestRowsHeap(mat, k))       
print(kWeakestRowsArray(mat, k))         
print(kWeakestRowsHashMap(mat, k))           