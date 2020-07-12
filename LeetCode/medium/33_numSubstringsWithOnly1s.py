# https://leetcode.com/problems/number-of-substrings-with-only-1s/


# Time O(n) | Space O(1)
def numSub(s):
    sum = count = 0
    for i in s:
        if i == '1':
            count += 1
            sum += count
        else:
            count = 0
    return sum%1000000007
    


def numSubII(s):
    ones_array = s.split('0')
    total = []
    for i in ones_array:
        if i:
            n = len(i)

            # (n*(n+1)//2) is the sum of natural number 1, 2, 3
            # basically 1+2+3+4+5.... approaches (n*(n+1)//2) 
            total.append(((n)*(n+1))//2)

    return sum(total)%(10**9+7)

s = "0110111"
print(numSubII(s))