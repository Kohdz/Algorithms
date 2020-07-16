# https://leetcode.com/problems/2-keys-keyboard/


# prime factorization | Time O(sqrt(N)) | Space O(1)
def minSteps(n):
    
    ans = 0
    
    d = 2
    
    while n > 1:
        
        while n % d == 0:
            ans += d
            n /= d
        d += 1
    return ans


def minStepsDP(n):

     # dp[x] = minimum number of steps to get x A on screen
    # how to divide the number x?
    # x can be expressed as a*b
    # lets say b is always higher than a
    # so highest value of b can be x:                   :x is prime (x cannot be divided)
    # or highest value of b can be some factor of x:    :x is not prime

    # if x is not prime, collect b as in clipboard and paste a -1 or (x//b- 1) times
    # collecting b 'As' in clipboard = dp[b] + 1 (get b `As`: dp[b] and then "copy": 1)
    # paste b `As` in (a-1) times    = a - 1 = x //b -1

    # so dp[x] = dp[b] + 1 + x//b - 1 --- where b is largest factor of x


    # dp[i]  = min number of steps

    dp = [i for i in range(n + 1)]

    # exception is 0 and 1, for which answer is 0
    dp[0] = dp[1] = 0


    for i in range(2, n + 1):

        for j in range(i - 1, 1, -1):

            if (i % j == 0):
                
                dp[i] = dp[j] + 1 + (i//j) - 1
                break

    return dp[n]

n = 3
print(minSteps(n)) # should return 3