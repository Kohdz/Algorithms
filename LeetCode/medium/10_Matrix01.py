# https: // leetcode.com/problems/01-matrix/


from collections import deque


def updateMatrix(matrix):

    queue = deque([])
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                queue.append((i, j))
            if matrix[i][j] == 1:
                matrix[i][j] = -1
    while queue:
        i, j = queue.popleft()
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[0]) and matrix[ni][nj] == -1:
                matrix[ni][nj] = matrix[i][j] + 1
                queue.append((ni, nj))
    return matrix


matrix = [[0, 0, 0],
          [0, 1, 0],
          [1, 1, 1]]


print(updateMatrix(matrix))
