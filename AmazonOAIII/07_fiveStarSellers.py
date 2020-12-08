import heapq


# Time: (N log N) | Space O(N)
#  O(N + klogN) w

def fiveStartReviews(productRatings, ratingsThreshold):

    n = len(productRatings)
    ans = 0
    cur_rating = sum(p[0]/p[1] for p in productRatings) / n * 100

    def diff(p):
        return (p[0]+1)/(p[1]+1) - p[0]/p[1]
    # create diff and store in heap & heapify

    heap = [[-diff(p)]+p for p in productRatings]
    heapq.heapify(heap)

    while cur_rating < ratingsThreshold:
        p_diff, p0, p1 = heapq.heappop(heap)
        # update current rating by adding the difference
        cur_rating = (cur_rating * n + (-p_diff) * 100) / n
        # maintain diff order in heap
        heapq.heappush(heap, [-diff([p0+1, p1+1]), p0+1, p1+1])
        ans += 1
    return ans


productRatings = [[[4, 4], [1, 2], [3, 6]]]
ratingsThreshold = [77]
output = [3]


for i in range(len(productRatings)):
    assert fiveStartReviews(
        productRatings[i], ratingsThreshold[i]) == output[i]
