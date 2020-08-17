# https://leetcode.com/problems/meeting-rooms-ii/

'''
Meeting Rooms I, II
Question 1

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

For example,

Given [[0, 30],[5, 10],[15, 20]],
return false.

Solution

The idea is pretty simple: first we sort the intervals in the ascending order of start; then we check for the overlapping of each pair of neighboring intervals. If they do, then return false; after we finish all the checks and have not returned false, just return true.

Sorting takes O(nlogn) time and the overlapping checks take O(n) time, so this idea is O(nlogn) time in total.

The code is as follows.
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
