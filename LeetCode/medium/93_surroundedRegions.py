# https://leetcode.com/problems/surrounded-regions/


def solve(board):
    """
    Do not return anything, modify board in-place instead.
    """
    if not board:
        return
    
    rows = len(board)
    cols = len(board[0]) 
    
    # rescue remaining 'O' cells from other 'O' cells on the border
    for i in range(rows):
        dfs(board, i, 0, rows, cols)
        dfs(board, i, cols - 1, rows, cols)
        
    for j in range(cols):
        dfs(board, 0, j, rows, cols)
        dfs(board, rows - 1, j, rows, cols)
        
    # update the cells
    transition_table = {'O': 'X', 'X':'X', 'alive':'O'}
    
    for i in range(rows):
        for j in range(cols):
            board[i][j] = transition_table[board[i][j]]

    return board
        
def dfs(board, i, j, rows, cols):
    
        
    if i < 0 or i>= rows or j < 0 or j >= cols or board[i][j] != 'O':
        return
    
    board[i][j] = 'alive'
        
    dfs(board, i-1, j, rows, cols)
    dfs(board, i+1, j, rows, cols)
    dfs(board, i, j-1, rows, cols)
    dfs(board, i, j+1, rows, cols)

board = [['X', 'X', 'X', 'X'], 
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X']]

print(solve(board))
