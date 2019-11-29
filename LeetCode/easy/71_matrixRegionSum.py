# https://leetcode.com/problems/range-sum-query-2d-immutable/
# [Matrix Region Sum]
# Given a matrix of integers and the top left and bottom right coordinates of a rectangular region within the matrix,
# find the sum of numbers falling inside the rectangle.
# Example:
# # matrix
# 1 2 3 4
# 5 6 7 8
# 9 0 1 2
# sum_matrix(matrix, [1, 1], [3, 2]) # => 24


def sum_matrix(matrix, cord1, cord2):

    print(matrix[cord1[1]][cord1[0]])
    print(matrix[cord2[1]][cord2[0]])

    sum = 0

    # for

    return 0


col = [1, 1]
row = [3, 2]

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 0, 1, 2]]

print(sum_matrix(matrix, col, row))
