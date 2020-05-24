# https://leetcode.com/problems/merge-intervals/

def merge(intervals):
        
    intervals.sort()
        
    merged = []
    for interval in intervals:
            
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
                
    return merged

intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
print(merge(intervals))