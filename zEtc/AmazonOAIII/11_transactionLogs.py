
from collections import Counter
from collections import defaultdict

# Time is O (n *m)


def fraudActivity(logs, threshold):
    hashMap = defaultdict(int)

    for log in logs:
        print(log)
        data = log[0].split(' ')
        userId1 = data[0]
        userId2 = data[1]
        transactions = data[2]

        if userId1 == userId2:
            hashMap[userId1] += 1

        hashMap[userId1] += 1
        hashMap[userId2] += 1

    output = []
    for key, value in hashMap.items():
        if value >= threshold:
            output.append(key)

    return output


transctionlog = [
    ['345366 89921 45'],
    ['029323 38239 23'],
    ['38239 345366 15'],
    ['029323 38239 77'],
    ['345366 38239 23'],
    ['029323 345366 13'],
    ['38239 38239 23']

]
threshold = 3


def find_frauds(transactions, threshold):
    if not transactions:
        return None
    cnt = Counter()
    for transaction in transactions:
        x = transaction[0].split()
        if x[0] != x[1]:
            cnt[x[0]] += 1
        cnt[x[1]] += 1

    ids = [userid for userid, occurence in cnt.items() if occurence >=
           threshold]
    return sorted(ids)


print(fraudActivity(transctionlog, threshold))

# Ouput: [345366 , 38239, 029323]

# Explanation:
# Given the following counts of userids, there are only 3 userids that meet or exceed the threshold of 3.
# 345366 - 4, 38239 - 5, 029323-3, 89921-1
