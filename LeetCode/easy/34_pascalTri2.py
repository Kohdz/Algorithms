# https://leetcode.com/problems/pascals-triangle-ii/

# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
# Note that the row index starts from 0.

# Input: 3
# Output: [1,3,3,1]


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


def getRow(rowIndex):
    result = []
    for i in range(rowIndex+1):
        result.append([])
        for j in range(i+1):
            if j in (0, i):
                result[i].append(1)
            else:
                result[i].append(result[i-1][j-1] + result[i-1][j])

    return result[rowIndex]


# def generate(numRows):
#     result = []
#     for i in range(numRows):
#         result.append([])
#         for j in range(i+1):
#             if j in (0, i):
#                 result[i].append(1)
#             else:
#                 result[i].append(result[i-1][j-1] + result[i-1][j])

#     return result


rowIndex = 3
print(getRow(rowIndex))
