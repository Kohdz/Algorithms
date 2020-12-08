# Top K Frequently Mentioned Keywords

import heapq
from collections import Counter


# Time O(k + N log(k))
# Space O(k + N log(N)); where n is the size of keywords
def topkfrequentII(keywords, reviews, k):
    elem = {}
    for review in reviews:
        for key in keywords:
            if key.lower() in review.lower():
                elem[key] = elem.get(key, 0)+1

    heap = []
    for key, freq in elem.items():
        heap.append((-freq, key))

    heapq.heapify(heap)
    return [heapq.heappop(heap)[1] for _ in range(k)]


def topKFrequent(keywords, reviews, k):

    heap = []
    totalWords = []

    for review in reviews:
        words = set(review.lower().split())
        totalWords.extend(words)

    wordFreq = Counter(totalWords)
    for word, freq in wordFreq.items():
        if word in keywords:
            heap.append((-freq, word))

    heapq.heapify(heap)
    return [heapq.heappop(heap)[1] for _ in range(k)]

    # print(totalWords)


k = 2
keywords = ["anacell", "cetracular", "betacellular"]
reviews = [
    "Anacell provides the best services in the city",
    "betacellular has awesome services",
    "Best services provided by anacell, everyone should use anacell",
]

# Output:
# ["anacell", "betacellular"]

# Explanation:
# "anacell" is occuring in 2 different reviews and "betacellular" is only occuring in 1 review.

print(topKFrequent(keywords, reviews, k))
