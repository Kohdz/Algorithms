'''Given an array of meeting time intervals consting of start and end times 
[[s1, e1], [s2, e2]...] (si < ei), find the minimum number of conferance
rooms required

Example 1
Input: [[0, 30], [5, 10], [15, 20]
Output = 2

Example 2
Input: [[7, 10], [2, 4]]
Output: 1'''

'''
https://www.youtube.com/watch?v=9ZsUM1ed05c
https://raw.githubusercontent.com/Kohdz/LeetcodeImages/master/253_01.png?token=AD3LTZ35KNLVQAF7R7DYGPK7I62HQ
Solution:

1. Sort the input array
2. Create a min-heap to store the end time of meetings that have had rooms
assigned to 
3. Start by pushing the end time of the first meeting to the heap
4. Loop through the rest of the array
    - compare the start time of the current meeting with the top element of the
    min heap
    - if they don't overlap, pop that element out from heap
    - push the end time of the current meeting into the min heap
5. After looping through all meeting, return the lenght of the heap
'''

import heapq

def minMeetingRooms(intervals):

    # if no meeting time intervals, then return 0
    if not intervals:
        return 0

    intervals.sort() 

    roomsUsed = [] 
    heapq.heappush(roomsUsed, intervals[0][1])
    
    for i in range(1, len(intervals)):
        # check if earliest meeting that ends in room, will finish before current meeting
        # if so, then remove earliest meeting
        if roomsUsed[0] <= intervals[i][0]:
            heapq.heappop(roomsUsed)
        heapq.heappush(roomsUsed, intervals[i][1])

    return len(roomsUsed)



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