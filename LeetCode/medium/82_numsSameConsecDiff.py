# https://leetcode.com/problems/numbers-with-same-consecutive-differences



def numsSameConsecDiffDFS(N, K):
    
    if N == 1:
        return [i for i in range(10)]

    ans = []
    def DFS(N, num):
        # base case
        if N == 0:
            return ans.append(num)

        tail_digit = num % 10
        # using set() to avoid duplicates when K == 0
        next_digits = set([tail_digit + K, tail_digit - K])

        for next_digit in next_digits:
            if 0 <= next_digit < 10: 
                new_num = num * 10 + next_digit
                DFS(N-1, new_num)

    for num in range(1, 10):
        DFS(N-1, num)

    return list(ans)

N = 2
K = 2
print(numsSameConsecDiffDFS(N, K))