# https://leetcode.com/problems/satisfiability-of-equality-equations/

'''
- Union all a and b for "a == b" in the equations.
- Then check each "a != b" in equations. If any pair of a and b belong to the same union set, or find(a) == find(b), then the given equality equations are not satisfiable.

Time: O(N) where NN is the length of equations

Space: O(1), assuming the size of the alphabet is O(1)


DFS Solution
https://leetcode.com/problems/satisfiability-of-equality-equations/discuss/234659/Python-solution
'''

class UnionFind:
    
    def __init__(self, n):
        self.parent = [i for i in range(26)]
        self.count = n

    def find(self, A):
        while A!= self.parent[A]:
            A = self.parent[A]
        return A

    def union(self, A, B):
        root_a = self.find(A)
        root_b = self.find(B)

        if root_a == root_b:
            return
        self.parent[root_a] = root_b
        self.count -= 1


def equationsPossible(equations):
    uf = UnionFind(len(equations))
    
    eqs, neqs = [], []
    for equation in equations:
        a, e, _, b = equation
        a , b = ord(a) -97, ord(b) - 97
        if e == '=':
            eqs.append((a, b))
        else:
            neqs.append((a, b))
    
    for a, b in eqs:
        uf.union(a, b)
    
    for a, b in neqs:
        if uf.find(a) == uf.find(b):
            return False
    return True

equations = ["a==b","b!=a"]
equations2 = ["b==a","a==b"]
print(equationsPossible(equations))
print(equationsPossible(equations2))