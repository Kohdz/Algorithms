# https://leetcode.com/problems/spiral-matrix-ii/


def generateMatrix(n):
    matrix = [[0] * n for _ in range(n)]
    num, layer, targetLayer = 1, 0, (n - 1) / 2

    while layer <= targetLayer:

        for j in range(layer, n - layer):
            matrix[layer][j] = num
            num += 1

        for i in range(layer + 1, n - layer):
            matrix[i][n - layer - 1] = num
            num += 1

        for j in range(n - layer - 2, layer - 1, -1):
            matrix[n - layer - 1][j] = num
            num += 1

        for i in range(n - layer - 2, layer, -1):
            matrix[i][layer] = num
            num += 1

        layer += 1

    return matrix
