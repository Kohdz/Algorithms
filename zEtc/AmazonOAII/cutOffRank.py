


import heapq

def cutOffRanks(num, cutOffRank, scores):

    heap = []

    for i, score in enumerate(scores):
        heapq.heappush(heap, -score)

    result = 0

    while heap and result < cutOffRank:

        # peek the max score 
        score = heap[0]
        while heap and heap[0] == score:
            heapq.heappop(heap)
            result += 1
    
    return result


# Time complexity: O(nlogn)
# Space complexity: O(logn)/O(n)
def cutOffRanksII(num, cutOffRank, scores):

    if cutOffRank >= num:
        return num

    rank = 0

    scores.sort()

    for i in reversed(range(num)):

        curr = scores[i]
        rank += 1

        while (i - 1) >= 0 and scores[i - 1] == curr:
            rank += 1
            i-= 1
        
        if rank >= cutOffRank:
            return len(scores) - 1
    
    return len(scores) - 1
            




num = 4
cutOffRank = 3
scores = [100, 50, 50, 25]


num2 = 4
cutOffRank2 = 5
scores2 = [2, 2, 3, 4, 5]

# print(cutOffRanks(num, cutOffRank, scores))
# print(cutOffRanks(num2, cutOffRank2, scores2))

print(cutOffRanksII(num, cutOffRank, scores))
print(cutOffRanksII(num2, cutOffRank2, scores2))

