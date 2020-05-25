# https://leetcode.com/problems/set-matrix-zeroes/solution/



def setZeroesBrute(matrix):

        
    R = len(matrix)
    C = len(matrix[0])
        
        
    rows, cols = set(), set()
    for i in range(R):
        for j in range(C):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)
                    
    for i in range(R):
        for j in range(C):

            if i in rows or j in cols:
                 matrix[i][j] = 0
                    

def setZeroes(matrix):

        
    is_col = False
    R = len(matrix)
    C = len(matrix[0])
        
    for i in range(R):
        # Since first cell for both first row and first column is the same i.e. matrix[0][0]
        # We can use an additional variable for either the first row/column.
        # For this solution we are using an additional variable for the first column
        # and using matrix[0][0] for the first row.
            
        if matrix[i][0] == 0:
            is_col = True
            
        for j in range(1, C):
            # If an element is zero, we set the first element of the corresponding row and column to 0
            if matrix[i][j]  == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0

    # Iterate over the array once again and using the first row and first column, update the elements.
    for i in range(1, R):
        for j in range(1, C):
            if not matrix[i][0] or not matrix[0][j]:
                matrix[i][j] = 0

    # See if the first row needs to be set to zero as well
    if matrix[0][0] == 0:
        for j in range(C):
            matrix[0][j] = 0

    # See if the first column needs to be set to zero as well        
    if is_col:
        for i in range(R):
            matrix[i][0] = 0


    return matrix

matrix1 = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]

test1_Sol = [
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

matrix2 = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]

test2_Sol = [
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

if setZeroes(matrix1) ==test1_Sol:
    print("Test 1 Passed")
else:
    print("Test 1 Failed")


if setZeroes(matrix2) == test2_Sol:
    print("Test 1 Passed")
else:
    print("Test 2 Failed")