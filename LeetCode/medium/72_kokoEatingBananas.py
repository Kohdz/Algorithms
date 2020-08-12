# https://leetcode.com/problems/koko-eating-bananas/
# https://www.youtube.com/watch?v=Sp2sRLcLND0

import math

def minEatingSpeed(piles, H):
    
    def feasible(speed):
            
        time = 0
        for banana in piles:
            time += math.ceil(banana / speed)
        return time <= H
    
    left, right = 1, max(piles)
    while left < right:
        mid = left + (right -left >> 1)
        
        if feasible(mid):
            right = mid
        else:
            left = mid + 1
    return left

H = 8
piles = [3,6,7,11]
# Output: 4

print(minEatingSpeed(piles, H))