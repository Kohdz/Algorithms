
def exist(board, word):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfsHelper(board, i, j, word, 0):
                return True
    return False


def dfsHelper(board, i, j, word, wordIndex):
    if wordIndex == len(word):
        return True

    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[wordIndex] != board[i][j]:
        return False

    board[i][j] = '#'

    found = dfsHelper(board, i + 1, j, word, wordIndex + 1) \
        or dfsHelper(board, i - 1, j, word, wordIndex + 1) \
        or dfsHelper(board, i, j + 1, word, wordIndex + 1) \
        or dfsHelper(board, i, j - 1, word, wordIndex + 1)

    board[i][j] = word[wordIndex]
    return found


board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]

word = "ABCCED"  # return true.
word2 = "SEE"  # return true.
word3 = "ABCB"  # return false.


if exist(board, word) == True:
    print("Test for word Passed")
else:
    print('Test for word Failed')

if exist(board, word2) == True:
    print("Test for word2 Passed")
else:
    print("Test for word2 Failed")

if exist(board, word3) == False:
    print("Test for word3 Passed")
else:
    print("Test for word3 Failed")
