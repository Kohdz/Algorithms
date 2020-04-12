# https://leetcode.com/problems/course-schedule/
# Topological Sort

import collections


def canFinish(numCourses, prerequisites):
    graph = collections.defaultdict(set)
    neighbors = collections.defaultdict(set)
    for course, pre in prerequisites:
        graph[course].add(pre)
        neighbors[pre].add(course)
    stack = [n for n in range(numCourses) if not graph[n]]
    count = 0
    while stack:
        node = stack.pop()
        count += 1
        for n in neighbors[node]:
            graph[n].remove(node)
            if not graph[n]:
                stack.append(n)
    return count == numCourses


NumCourses = 2
prerequisites = [[1, 0], [0, 1]]

# numCourses1 = 2
# prerequisites2 = [[1,0]]

print(canFinish(NumCourses, prerequisites))
