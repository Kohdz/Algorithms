# https://leetcode.com/problems/last-stone-weight/
# https://www.youtube.com/watch?v=-1jxt_DPl48&list=PLEJXowNB4kPwCPVjDv6KsAsThtDOCQUok

import heapq

# heap solution
# Sort stones descendingly in PriorityQueue, then pop out pair by 
# pair, compute the difference between them and add back to PriorityQueue.

# Put all elements into a priority queue.
# Pop out the two biggest, push back the difference,
# until there are no more two elements left.


# Complexity
# Time O(NlogN)
# Space O(N)

def lastStoneWeightHeap(stones):
    # sign-flip
    for i in range( len(stones) ):
        stones[i] *= -1
    
    # build min-heap in-place
    heapq.heapify( stones )
    
    # carry out stone-smash process, defined in description
    while len(stones) > 1:
        first = heapq.heappop( stones )
        second = heapq.heappop( stones )
        diff = first-second
        if diff != 0:
            heapq.heappush( stones, diff )
                            
                            
    # report final status        
    if len(stones):
        return -stones[0]
    else:
        return 0

# recursive sort
def lastStoneWeightRec(stones):
    if len(stones) == 1: return stones[0]
    stones.sort()
    return lastStoneWeightRec([stones.pop() - stones.pop()] + stones)

# pop and compare
def lastStoneWeightSortPop(stones):
    while len(stones)>1:
        stones.sort()
        m1=stones.pop()
        m2=stones.pop()
        if m1 != m2:
            stones.append(abs(m1-m2))         
    return stones[0] if stones else 0


A = [2,7,4,1,8,1]
# output 1

print(lastStoneWeightJeap(A))