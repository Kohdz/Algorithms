# https://leetcode.com/problems/pascals-triangle/

# Given a non-negative integer numRows, generate
# the first numRows of Pascal's triangle.

# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]


def generate(numRows):
    result = []
    for i in range(numRows):
        result.append([])
        for j in range(i+1):
            if j in (0, i):
                result[i].append(1)
            else:
                result[i].append(result[i-1][j-1] + result[i-1][j])

    return result


numRows = 5

print(generate(numRows))
