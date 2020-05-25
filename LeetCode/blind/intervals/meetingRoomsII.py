# Given an array of meeting time intervals consting of start and end times 
# [[s1, e1], [s2, e2]...] (si < ei), find the minimum number of conferance
# rooms required

# Example 1
# Input: [[0, 30], [5, 10], [15, 20]
# Output = 2

# Example 2
# Input: [[7, 10], [2, 4]]
# Output: 1


import heapq

def minMeetingRooms(intervals):

    # if no meeting time intervals, then return 0
    if not intervals:
        return 0

    # process each meeting in increasig start times for intervals
    intervals.sort(key = lambda x: x[0]) # O (n log n ) where n is number of elements in list

    # room heap to keep track of O (n log n) runtime where n is 
    rooms = [intervals[0][1]]

    # number of elements in intervals
    for meeting in intervals[1:]:
        # check if earliest meeting that ends in room, will finish before current meeting
        # if so, then remove earliest meeting
        if rooms[0] <= meeting[0]:
            heapq.heappop(rooms)
        heapq.heappush(rooms, meeting[1])

    return len(rooms)



intervals1 = [[0, 30], [5, 10], [15, 20]]

intervals2 = [[7, 10], [2, 4]]


if minMeetingRooms(intervals1) == 2:
    print("Test 1 Passed")
else:
    print("Test 1 Failed")

if minMeetingRooms(intervals2) == 1:
    print("Test 2 Passed")
else:
    print("Test 2 Failed")