# https://leetcode.com/problems/non-overlapping-intervals/
# https://www.youtube.com/watch?v=BTObFnHbD4U

# The heuristic is: always pick the interval with the earliest end time. Then you can
#  get the maximal number of non-overlapping intervals. (or minimal number to remove).
# This is because, the interval with the earliest end time produces the maximal capacity
#  to hold rest intervals.

def eraseOverlapIntervalsEndSort(intervals):

    # we sort intervals according to end-point
    intervals.sort(key = lambda x: x[1])
    
    minimum_to_erase = 0
    last = 0
    
    # go over intervals, only from second one, because 1st one is for sure not to be erased
    # count how many intervals overlap with last intervals
    for i in range(1, len(intervals)):
    
        #if start-point is before end-point of last intervals then there's an overlap
        if intervals[i][0] < intervals[last][1]:
            minimum_to_erase += 1
            
        else:
            last = i;
            
    #result
    return minimum_to_erase


def eraseOverlapIntervalsSortFront(intervals):
    
    if len(intervals) < 2:
        return 0
    
    intervals.sort()
    count, last_included = 0, 0
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[last_included][1]: # overlap
            count += 1
            if intervals[i][1] < intervals[last_included][1]:
                last_included = i
        else:
            last_included = i
    return count


