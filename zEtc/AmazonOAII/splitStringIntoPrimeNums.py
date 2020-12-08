import math
from math import ceil

def is_prime(n):
    dp = {0: False, 1: False, 2:True, 3: True}
    if n in dp:
        return dp[n]

    v = int(ceil(math.sqrt(n)))
    for i in range(2, v+1):
        if n % i == 0:
            dp[n] = False
            return False
    dp[n] = True
    return True

def countPrimeStrings(primeStr):
    memo = {}

    if primeStr in memo:
        return memo[primeStr]
    if not primeStr:
        return 1

    val = ''
    total = 0
    for i in range(len(primeStr)):
        val += primeStr[i]
        if is_prime(int(val)):
            total += countPrimeStrings(primeStr[i+1:])

    memo[primeStr] = total
    return memo[primeStr]


class Solution:
    def primeString(self, curr, prime_set, stck, prime_lst):
        if not curr:
            prime_set.append(stck)
            return
        for i in range(1, len(curr) + 1):
            next_ele = int(curr[:i])
            if prime_lst[next_ele]:
                self.primeString(curr[i:], prime_set, stck + [next_ele], prime_lst)

    def countPrimes(self, input_str):
        int_input = int(input_str)
        if int_input == 0 or int_input == 1: return 0

        cnt = [True] * (int_input + 1)
        cnt[0] = cnt[1] = False
        for i in range(2,int((int_input+1)**0.5) + 1):
            for p in range(i*i, int_input+1, i):
                cnt[p] = False
        curr = []
        self.primeString(input_str, curr, [], cnt)
        return len(curr) % 1000000007


# output 6
# [11, 3, 7, 3]
# [113, 7, 3]
# [11, 3, 73]
# [1137]
# [113, 73]
# [11, 376]
primeStr = '333'
# print(memo[primeStr])
print(countPrimeStrings(primeStr))
