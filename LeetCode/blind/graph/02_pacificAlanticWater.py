# https://leetcode.com/problems/pacific-atlantic-water-flow/


def pacificAtlantic(matrix):

    # Check for an empty graph.
    if not matrix:
        return []

    p_visited = set()
    a_visited = set()
    rows, cols = len(matrix), len(matrix[0])
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def traverse(i, j, visited):
        if (i, j) in visited:
            return
        visited.add((i, j))

        # Traverse neighbors.
        for direction in directions:
            next_i, next_j = i + direction[0], j + direction[1]
            if 0 <= next_i < rows and 0 <= next_j < cols:

                # Add in your question-specific checks.
                if matrix[next_i][next_j] >= matrix[i][j]:
                    traverse(next_i, next_j, visited)

    for row in range(rows):
        traverse(row, 0, p_visited)
        traverse(row, cols - 1, a_visited)

    for col in range(cols):
        traverse(0, col, p_visited)
        traverse(rows - 1, col, a_visited)

    return list(p_visited & a_visited)


matrix = [[1, 2, 2, 3, 5],
          [3, 2, 3, 4, 4],
          [2, 4, 5, 3, 1],
          [6, 7, 1, 4, 5],
          [5, 1, 1, 2, 4]]

SOL = [(1, 3), (3, 0), (3, 1), (1, 4), (0, 4), (2, 2), (4, 0)]


print(pacificAtlantic(matrix) == SOL)
