# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets
# https://leetcode.com/discuss/general-discussion/786126/python-powerful-ultimate-binary-search-template-solved-many-problems


def minDays(bloomDay, m, k):
    
    def feasible(days):
        # num of adjacent | m 
        bonquets, flowers = 0, 0
        for bloom in bloomDay:
            if bloom > days:
                flowers = 0
            else:
                bonquets += (flowers + 1) // k
                flowers = (flowers + 1) % k
        return bonquets >= m

    if len(bloomDay) < m * k:
        return -1
    left, right = 1, max(bloomDay)
    while left < right:
        mid = left + (right - left >> 1)
        if feasible(mid):
            right = mid
        else:
            left = mid + 1
    return left

k = 1
m = 3
bloomDay = [1,10,3,10,2]
print(minDays(bloomDay, m, k))