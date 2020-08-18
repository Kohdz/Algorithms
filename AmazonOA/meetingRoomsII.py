# https://leetcode.com/problems/meeting-rooms-ii/

'''
Meeting Rooms I, II
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],…] (si < ei), 
find the minimum number of conference rooms required.

Example 1:
Input: [[0, 30],[5, 10],[15, 20]]
Output: 2

Example 2:
Input: [[7,10],[2,4]]
Output: 1
'''

def meeting_room(intervals):

    meetings_num = len(intervals)
    start = [0] * meetings_num
    end = [0] * meetings_num

    for index in range(meetings_num):
        start[index] = intervals[index][0]
        end[index] = intervals[index][1]

    start.sort()
    end.sort()

    end_i = 0
    rooms = 0
    for index in range(meetings_num):
        if start[index] < end[end_i]:
            rooms += 1
        else:
            end_i += 1

    return rooms


intervals =  [[0, 30],[5, 10],[15, 20]]
# return false
print(meeting_room(intervals))