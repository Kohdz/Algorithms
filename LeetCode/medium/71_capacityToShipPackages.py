# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/


def feasible(capacity, weights, D):
    days = 1
    total = 0
    for weight in weights:
        total += weight
        
        # too heavy, wait for the next day
        if total > capacity:
            total = weight
            days += 1
            
            # cannot ship within D days
            if days > D:
                return False
    return True

def shipWithinDays(weights, D):

    left, right = max(weights), sum(weights)
    while left < right:
        mid = left + (right - left >> 1)
        if feasible(mid, weights, D):
            right = mid
        else:
            left = mid + 1
    return left

D = 5
weights = [1,2,3,4,5,6,7,8,9,10]
print(shipWithinDays(weights, D))