# https://leetcode.com/problems/ones-and-zeroes/

# 3d-DP optimized to 2D space: dp[j][k]: i dimension is optimized to be used in-place
# Notice the j and k should be changed to update FROM LARGER TO SMALLER
# https://snowan.gitbook.io/study-notes/leetcode/english-solution/474.ones-and-zeros-en
# This is a multi-dimensional cost 0-1 knapsack problem with two backpack sizes, 0 number and 1 number.


def findMaxForm(strs, m, n):
    # we are traversing reverse to prevent subproblems from overlapping
    # consider string "01" and m = 5, n = 3 and draw the matrix from normal
    #order and in reverse order, you'll understand
    
    # the lower limit is number of zeros and ones, because before that you wont find match
    dp = [[0] * (n + 1) for _ in range(m +1)]
    
    for s in strs:
        
        zeros, ones = s.count('0'), s.count('1')
        
        for i in range(m, zeros - 1, -1):
            
            for j in range(n, ones -1, - 1):
                
                # dp[i][j] indicates it has i zeros ans j ones,
                # can this string be formed with those ?
                
                dp[i][j] = max( 1 + dp[i - zeros][j - ones], dp[i][j])
                
            # print(dp)
            
    return dp[-1][-1]

n = 3
m = 5
strs = ["10","0001","111001","1","0"]
# Output: 4

print(findMaxForm(strs, m, n))