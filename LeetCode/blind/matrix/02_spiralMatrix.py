def spiralOrder(matrix):
    if not matrix:
        return []

    firstRow, firstCol = 0, 0
    rows, cols = len(matrix), len(matrix[0])
    result = []

    while rows > 0 and cols > 0:
        lastRow = firstRow + rows - 1
        lastCol = firstCol + cols - 1

        # Top left to right
        for i in range(cols):
            result.append(matrix[firstRow][firstCol + i])
        # Right top to bottom
        for i in range(1, rows):
            result.append(matrix[firstRow + i][lastCol])
        # Bottom right to left        lastRow = firstRow + rows - 1
        lastCol = firstCol + cols - 1
        for i in range(1, cols):
            if firstRow != lastRow:
                result.append(matrix[lastRow][lastCol - i])
        # Left bottom to top
        for i in range(1, rows - 1):
            if firstCol != lastCol:
                result.append(matrix[lastRow - i][firstCol])

        # Next layer
        firstRow += 1
        firstCol += 1
        rows -= 2
        cols -= 2

    return result


matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(spiralOrder(matrix1))
