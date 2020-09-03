
class UnionFind:
    
    def __init__(self, n):
        self.parent = [i for i in range(n)]
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
