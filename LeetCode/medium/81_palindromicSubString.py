# https://leetcode.com/problems/palindromic-substrings/
# https://www.youtube.com/watch?v=EIf9zFqufbU

def countString(s):
    def expand(left: int, right: int) -> int:
        count = 0
        while left >= 0 and right < n and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count

    n = len(s)
    ans = 0
    for i in range(n):
        ans += 1 + expand(i - 1, i + 1) + expand(i, i + 1)
    return ans

def countStringDP(s):
    count = 0
    n = len(s)
    dp = [[True]*n for _ in range(n)]
    for k in range(1,n):
        for i in range(n-k):
            j = i+k
            if j == i+1:
                dp[i][j] = (s[i]==s[j])
            else:
                dp[i][j] = ((s[i]==s[j]) and dp[i+1][j-1])
            if dp[i][j]:
                count += 1
    return count + n

s = 'abc'
print(countString(s))

