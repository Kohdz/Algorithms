
# Time O(n^4) | Space O(n^3) 
def squareOfZerosRec(matrix):
    lastIdx = len(matrix)  - 1
    return hasSquareOfZeros(matrix, 0, 0, lastIdx, lastIdx, {}) 


def hasSquareOfZeros(matrix, r1, c1, r2, c2, cache):
    if r1 >= r2 or c1 >= c2:
        return False

    key = str(r1) + "-" + str(c1) + "-" + str(r2) + "-" + str(c2)
    if key in cache:
        return cache[key]

    cache[key] = (
        isSquareOfZeros(matrix, r1, c1, r2, c2)
        or hasSquareOfZeros(matrix, r1 + 1, c1 + 1, r2 - 1, c2 - 1, cache)
        or hasSquareOfZeros(matrix, r1, c1 + 1, r1 - 1, c2, cache)
        or hasSquareOfZeros(matrix, r1 + 1, c1, r2, c2-1, cache)
        or hasSquareOfZeros(matrix, r1 + 1, c1 + 1, r2, c2, cache)
        or hasSquareOfZeros(matrix, r1, c1, r2 - 1, c2 - 1, cache)
    )

    return cache[key]

def isSquareOfZeros(matrix, r1, c1, r2, c2):

    for row in range(r1, r2 + 1):
        if matrix[row][c1] != 0 or matrix[row][c2] != 0:
            return False

    for col in range(c1, c2 + 1):
        if matrix[r1][col] != 0 or matrix[r2][col] != 0:
            return False
    
    return True



# Time O(n^4) | Space O(n^3)
def squareOfZerosIter(matrix):
    n = len(matrix)
    for topRow in range(n):
        for leftCol in range(n):
            squareLenght = 2
            while squareLenght <= n - leftCol and squareLenght <= n - topRow:
                bottomRow = topRow + squareLenght - 1
                rightCol = leftCol + squareLenght - 1
                if isSquareOfZeros(matrix, topRow, leftCol, bottomRow, rightCol):
                    return True
                squareLenght += 1
        
        return False


# O(n^3) Time | O(n^3) Space
def squareOfZerosRecOptimizes(matrix):
    infoMatrix = preComputedNumsOfZeros(matrix)
    lastIdx = len(matrix)  - 1
    return hasSquareOfZerosII(infoMatrix, matrix, 0, 0, lastIdx, lastIdx, {}) 



def isSquareOfZerosII(infoMatrix, r1, c1, r2, c2):

    squareLenght = c2 - c1 + 1
    hasTopBoarder = infoMatrix[r1][c1]["numZerosRight"] >= squareLenght
    hasLeftBoarder = infoMatrix[r1][c1]["numZerosBelow"] >= squareLenght
    hasBottomBoarder = infoMatrix[r2][c1]["numZerosRight"] >= squareLenght
    hasRightBoarder = infoMatrix[r1][c2]["numZerosBelow"] >= squareLenght

    return hasTopBoarder and hasLeftBoarder and hasBottomBoarder and hasRightBoarder



def hasSquareOfZerosII(infoMatrix, matrix, r1, c1, r2, c2, cache):
    if r1 >= r2 or c1 >= c2:
        return False

    key = str(r1) + "-" + str(c1) + "-" + str(r2) + "-" + str(c2)
    if key in cache:
        return cache[key]

    cache[key] = (
        isSquareOfZeros(matrix, r1, c1, r2, c2)
        or hasSquareOfZerosII(infoMatrix, matrix, r1 + 1, c1 + 1, r2 - 1, c2 - 1, cache)
        or hasSquareOfZerosII(infoMatrix, matrix, r1, c1 + 1, r1 - 1, c2, cache)
        or hasSquareOfZerosII(infoMatrix, matrix, r1 + 1, c1, r2, c2-1, cache)
        or hasSquareOfZerosII(infoMatrix, matrix, r1 + 1, c1 + 1, r2, c2, cache)
        or hasSquareOfZerosII(infoMatrix, matrix, r1, c1, r2 - 1, c2 - 1, cache)
    )


def preComputedNumsOfZeros(matrix):

    infoMatrix = [[x for x in row] for row in matrix]

    n = len(matrix)
    for row in range(n):
        for col in range(n):
            
            numZeros = 1 if matrix[row][col] == 0 else 0
            infoMatrix[row][col] = {
                "numZerosBelow": numZeros,
                "numZerosRight": numZeros
            }
    
    lastIdx = len(matrix) - 1
    for row in reversed(range(n)):
        for col in reversed(range(n)):
            if matrix[row][col] == 1:
                continue
            if row < lastIdx:
                infoMatrix[row][col]["numZerosBelow"] += infoMatrix[row + 1]["numZerosBelow"]
            if col < lastIdx:    
                infoMatrix[row][col]["numZerosRight"] += infoMatrix[row + 1]["numZerosRight"]

    return infoMatrix


matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    ]
print(squareOfZerosRec(matrix))