import collections
import heapq
import re


def topKFrequentMentionedKeywords(keywords, reviews, k):
    """
    :type keywords: List[str]
    :type reviews: List[str]
    :type k: int
    :rtype: List[str]
    """

    data_value_dict = collections.Counter()
    key_value_dict = set(keywords)
    res = []

    for review in reviews:
        temp_list = review.lower().split(' ')

        for value in temp_list:
            value = re.sub('[^a-z]', '', value)

            if value in key_value_dict:
                data_value_dict[value] += 1

    res = heapq.nsmallest(k, data_value_dict,
                          key=lambda x: (-data_value_dict[x], x))

    return res


numFeatures = 6
topFeatures = 2
possibleFeatures = ["storage", "battery",
                    "hover", "alexa", "waterproof", "solar"]
numFeaturesRequested = 7
featureRequested = ["I wish my kindle had even more storage!", "I wish the battery life on my kindle lasted 2 years", "I read in the bath and would enjoy a waterproof kindle", "Waterproof and increased battery are my top two requests",
                    "I want to take my kindle into the shower. Waterproof please waterproof!", "It would be neat if my kindle would hover on my desk when not in use", "How cool would it be if my kindle charged in the sun via solar power?"]


#  top_K_freq_keywords(keywords, reviews, k):
print(topKFrequentMentionedKeywords(
    possibleFeatures, featureRequested, topFeatures))
