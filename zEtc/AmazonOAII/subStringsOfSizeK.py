# f size K such that there is exactly one character that is repeated once.

from collections import Counter


def slidWindow(word, K):
    
    if len(word) < K:
        return ""

    left = 0
    output = [] # also try set()
    counter = Counter()

    for right in range(len(word)):
        
        currWord = word[right]
        counter[currWord] += 1

        while right - left + 1 > K:
            leftWord = word[left]
            counter[leftWord] -= 1

            if not counter[leftWord]:
                del counter[leftWord]
            left += 1

        if len(counter) + 1 == K and right - left + 1 == K:
            output.append(word[left: right + 1])


    return output

K = 4
word = 'awaglk'

K2 = 5
word2 = 'democracy'

K3 = 4
word3 = 'wawaglknagagwunagkwkwagl'
print(slidWindow(word, K))
print(slidWindow(word2, K2))
print(slidWindow(word3, K3))


# Output:
# [awag]

# Explanation:
# The substrings are {awag, wagl, aglk}
# The answer is awag as it has 3 distinct characters in a string of size 4, and only one character is repeated twice.