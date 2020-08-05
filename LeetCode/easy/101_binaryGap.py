# https://leetcode.com/problems/binary-gap/submissions/


def binaryGap(N):

    curr, prev = 0, -1
    max_gap = 0 
    
    while N > 0:
        if N & 1:
            if prev != -1:
                max_gap = max(max_gap, curr- prev)
            prev = curr
        curr += 1
        N >>= 1
    return max_gap

N = 22
print(binaryGap(N))