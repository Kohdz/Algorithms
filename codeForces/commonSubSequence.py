# https://codeforces.com/contest/1382/problem/A




def commonSubSequence(len_a, len_b, A, B):

    pass
    





testCases = [[4, 5, [10, 8, 6, 4], [1, 2, 3, 4, 5]], 
            [1, 1, [3], [3]], 
            [1, 1, [3], [2]], 
            [5, 3, [1000, 2, 2, 2, 3],[3, 1, 5]], 
            [5, 5, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]]

solutions = [['YES', 1, 4], 
            ['YES', 1, 3], 
            ['NO'],
            ['YES', 1, 3], 
            ['YES', 1, 2]]

print(commonSubSequence(testCases[0][0], testCases[0][1], testCases[0][2], testCases[0][3]) == solutions[0])

# for i in range(len(testCases)):
#     print(commonSubSequence(testCases[i][0], testCases[i][1], testCases[i][2], testCases[i][3]) == solutions[i])

