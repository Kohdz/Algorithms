# https://leetcode.com/problems/iterator-for-combination/
from itertools import combinations
from collections import deque

class CombinationIterator:

    def __init__(self, characters, combinationLength):
        self.combinations = deque(''.join(comb) for comb in combinations(characters, combinationLength))

    def nexts(self):
        return self.combinations.popleft()

    def hasNext(self):
        return len(self.combinations) != 0

class CombinationIteratorDFS:

    def __init__(self, characters: str, combinationLength: int):
        self.result = []
        self.dfs(characters, "", combinationLength, 0)

    def next(self) -> str:
        if len(self.result):
            return self.result.pop(0)

    def hasNext(self) -> bool:
        return len(self.result) > 0
        
    def dfs(self, s, path, k, idx):
        if len(path) == k:
            self.result.append(path)
            return
        for i in range(idx, len(s)):
            self.dfs(s, path + s[i], k, i+1)


characters = 'abc'
combinationLenght = 2
ci = CombinationIterator(characters, combinationLenght)

ci_genext = ci.nexts()
print(ci_genext)

ci_hasNext = ci.hasNext()
print(ci_hasNext)

ci_genext2 = ci.nexts()
print(ci_genext2)

ci_hasNext2 = ci.hasNext()
print(ci_hasNext2)

ci_genext3 = ci.nexts()
print(ci_genext3)

ci_hasNext3 = ci.hasNext()
print(ci_hasNext3)

# iterator.next(); // returns "ab"
# iterator.hasNext(); // returns true
# iterator.next(); // returns "ac"
# iterator.hasNext(); // returns true
# iterator.next(); // returns "bc"
# iterator.hasNext(); // returns false