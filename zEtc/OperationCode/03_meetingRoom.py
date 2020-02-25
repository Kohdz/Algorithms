# [Meeting Rooms]
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
#  determine if a person could attend all meetings.
# Input: [[0,30],[5,10],[15,20]]
# Output: false
# Input: [[7,10],[2,4]]
# Output: true


def AttendMeeting(times):
    start = []
    end = []
    for i in range(len(times)):
        start.append(times[i][0])
        end.append(times[i][1])

    start.sort()
    end.sort()
    print(start)
    print(end)

    for i in range(len(times)-1):
        if start[i+1] < end[i]:
            return False

    return True


time1 = [[0, 30], [5, 10], [15, 20]]
time2 = [[7, 10], [2, 4]]
print(AttendMeeting(time1))
