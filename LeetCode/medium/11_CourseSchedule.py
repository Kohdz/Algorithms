# https://leetcode.com/problems/course-schedule/
# Topological Sort

import collections


def canFinish(numCourses, prerequisites):
        
    graph = { n: [] for n in range(numCourses)}
    marks = {n: 0 for n in range(numCourses)}
        
    for course, prereq in prerequisites:
        graph[prereq].append(course)
            
    for node in range(numCourses):
        if marks[node] == 0:
            if not dfs(node, graph, marks):
                return False
                
    return True
    
def dfs(node, graph, marks):
        
    marks[node] = 1
        
    for neighbor in graph[node]:
        if marks[neighbor] == 0:
            if not dfs(neighbor, graph, marks):
                return False
        elif marks[neighbor] == 1:
            return False
            
            
    marks[node] = 2
    return True


NumCourses = 2
prerequisites = [[1, 0], [0, 1]]

# numCourses1 = 2
# prerequisites2 = [[1,0]]

print(canFinish(NumCourses, prerequisites))
