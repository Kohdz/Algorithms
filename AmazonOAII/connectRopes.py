# Given n ropes of different lengths, we need to connect these ropes into one rope. We can connect 
# only 2 ropes at a time. The cost required to connect 2 ropes is equal to sum of their lengths. The
#  length of this connected rope is also equal to the sum of their lengths. This process is repeated 
#  until n ropes are connected into a single rope. Find the min possible cost required to connect all ropes.

# Input: ropes = [8, 4, 6, 12]
# Output: 58
# Explanation: The optimal way to connect ropes is as follows
# 1. Connect the ropes of length 4 and 6 (cost is 10). Ropes after connecting: [8, 10, 12]
# 2. Connect the ropes of length 8 and 10 (cost is 18). Ropes after connecting: [18, 12]
# 3. Connect the ropes of length 18 and 12 (cost is 30).
# Total cost to connect the ropes is 10 + 18 + 30 = 58


# Time Complexity O(nlogn)
# Space complexity O(n)

from heapq import heappush, heappop, heapify

def min_cost(ropes):
    cost = 0
    heapify(ropes)
    if len(ropes) == 1: return 0
    while len(ropes) > 1:
        sum = heappop(ropes) + heappop(ropes)
        cost += sum
        heappush(ropes, sum)
    return cost


def connectSticks(sticks):
    """
    :type sticks: List[int]
    :rtype: int
    """
    if len(sticks) <= 1:
        return 0 
    
    ans = 0
    heapify(sticks)
    while len(sticks) >= 2:
        num1, num2 = heappop(sticks), heappop(sticks)
        ans += num1 + num2
        heappush(sticks, num1 + num2)
    
    return ans

def connectRopes(ropes):
    heapify(ropes)
    cost = 0
    while len(ropes) > 1:
        cur = heappop(ropes) + heappop(ropes)
        cost += cur
        heappush(ropes, cur)
    return cost

    
ropes1 = [8, 4, 6, 12] # output = 58

ropes2  = [1, 2, 5, 10, 35, 89] # output = 224

ropes3 = [2, 2, 3, 3] # output = 20

ropes4= [20, 4, 8, 2] # output 54


print(min_cost(ropes1))
print(min_cost(ropes2))
print(min_cost(ropes3))
print(min_cost(ropes4))
