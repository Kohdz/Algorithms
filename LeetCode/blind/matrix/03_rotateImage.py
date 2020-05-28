# https://leetcode.com/problems/rotate-image/


def rotate(matrix):
    if not matrix:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    # we divide by two because we are using a two pointer approach
    for i in range(rows // 2):
        for j in range(cols):
            matrix[i][j], matrix[rows - i -
                                 1][j] = matrix[rows - i - 1][j], matrix[i][j]

    for i in range(rows):
        # note that your ranging through i
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    return matrix


matrix = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]

solution = [
    [15, 13, 2, 5],
    [14, 3, 4, 1],
    [12, 6, 8, 9],
    [16, 7, 10, 11]
]
if rotate(matrix) == solution:
    print("Test 1 Passed")
else:
    print("Test 1 Failed")
