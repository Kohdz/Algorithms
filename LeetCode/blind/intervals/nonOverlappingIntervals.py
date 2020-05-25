# https://leetcode.com/problems/non-overlapping-intervals/

def eraseOverlapIntervals(intervals):
        
    end, cnt = float('-inf'), 0
    intervals.sort(key=lambda x: x[1])
      
    for i in intervals:
        if i[0] >= end: 
            end = i[1]
        else: 
            cnt += 1
    return cnt

intervals =  [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.

print(eraseOverlapIntervals(intervals))