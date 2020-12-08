# https://leetcode.com/problems/top-k-frequent-words/
# The comparison of strings is case-insensitive. If keywords are mentioned an equal number of times in reviews, sort alphabetically.


# def topKFrequent(words, k):

#     counter = Counter(words)

#     heap = []
#     for key, count in counter.items():
#         heappush(heap, (-count, key))

#     ans = []

#     for _ in range(k):
#         popped = heappop(heap)
#         ans.append(popped[1])

#     return ans


# words = ["i", "love", "leetcode", "i", "love", "coding"]
# k = 2

# print(topKFrequent(words, k))

import heapq
from collections import defaultdict
from re import sub
import re
from collections import Counter


class Element:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq


# def topKFrequent(k, keywords, reviews):
#     '''
#     k: int
#     keywwords: list of string
#     reviews: list of string
#     '''
#     word_list = []

#     for review in reviews:
#         word_list += set(review.lower().replace('[^a-z0-9]', '').split())

#     count = Counter(word_list)

#     heap = []

#     for word, freq in count.items():
#         if word in keywords:
#             heapq.heappush(heap, Element(word, freq))
#             if len(heap) > k:
#                 heapq.heappop(heap)

#     return [heapq.heappop(heap).word for _ in range(k)][::-1]


# k = 2
# keywords = ["anacell", "cetracular", "betacellular"]
# reviews = [
#     "Anacell provides the best services in the city",
#     "betacellular has awesome services",
#     "Best services provided by anacell, everyone should use anacell",
# ]
# print(topKFrequent(k, keywords, reviews))

# def topkII(numFeatures, topFeatures, possibleFeatures, numFeaturesRequested, featureRequested):
#     pass


# numFeatures = 6
# topFeatures = 2
# possibleFeatures = ["storage", "battery",
#                     "hover", "alexa", "waterproof", "solar"]
# numFeaturesRequested = 7
# featureRequested = ["I wish my kindle had even more storage!", "I wish the battery life on my kindle lasted 2 years", "I read in the bath and would enjoy a waterproof kindle", "Waterproof and increased battery are my top two requests",
#                     "I want to take my kindle into the shower. Waterproof please waterproof!", "It would be neat if my kindle would hover on my desk when not in use", "How cool would it be if my kindle charged in the sun via solar power?"]

# output = ["waterproof", 'battery]


def top_K_freq_keywords(keywords, reviews, k):
    if not k or not keywords or not reviews:
        return []
    keys = set(keywords)
    word_count = defaultdict(int)
    for rev in reviews:
        words = rev.lower().split(" ")
        added = set()
        for word in words:
            word = sub("[^a-z]", "", word)
            if word in keys and word not in added:
                word_count[word] += 1
                added.add(word)
    # result = heapq.nsmallest(k, word_count, key=lambda x: (-word_count[x], x))
    result = sorted(word_count.keys(), key=lambda x: (-word_count[x], x))
    return result[:k]


keywords1 = ["anacell", "betacellular",
             "cetracular", "deltacellular", "eurocell"]
reviews1 = [
    "I love anacell Best services; Best services provided by anacell",
    "betacellular has great services",
    "deltacellular provides much better services than betacellular",
    "cetracular is worse than anacell",
    "Betacellular is better than deltacellular.",
]
k = 2

#output = ["betacellular", "anacell"]
print(top_K_freq_keywords(keywords1, reviews1, k))
