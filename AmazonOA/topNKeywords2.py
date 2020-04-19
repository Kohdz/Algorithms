# Time complexity: O(RW + NlogN)
# Space complexity: O(N)
# where
# N is size of keywords,
# R is size of reviews,
# W is maximum length review


import heapq
import collections
from collections import defaultdict
from re import sub
import re
from collections import Counter


def top_K_freq_keywords(keywords, reviews, k):
    if reviews is None or not len(reviews):
        return []
    if keywords is None or not len(keywords):
        return []
    if k == 0:
        return []
    # count number of reviews where the word appears
    review_freq = collections.Counter()
    keywords = set(keywords)
    for review in reviews:
        seen = set()
        for word in map(lambda x: x.lower(), re.findall(r'\w+', review)):
            if word in keywords and word not in seen:
                review_freq[word] += 1
                seen.add(word)
    candidates = [(-freq, word) for word, freq in review_freq.items()]
    heapq.heapify(candidates)
    res = [heapq.heappop(candidates)[1] for _ in range(k)]
    return res


numFeatures = 6
topFeatures = 2
possibleFeatures = ["storage", "battery",
                    "hover", "alexa", "waterproof", "solar"]
numFeaturesRequested = 7
featureRequested = ["I wish my kindle had even more storage!", "I wish the battery life on my kindle lasted 2 years", "I read in the bath and would enjoy a waterproof kindle", "Waterproof and increased battery are my top two requests",
                    "I want to take my kindle into the shower. Waterproof please waterproof!", "It would be neat if my kindle would hover on my desk when not in use", "How cool would it be if my kindle charged in the sun via solar power?"]


#  top_K_freq_keywords(keywords, reviews, k):
print(top_K_freq_keywords(possibleFeatures, featureRequested, topFeatures))

# output = ["waterproof", 'battery]
