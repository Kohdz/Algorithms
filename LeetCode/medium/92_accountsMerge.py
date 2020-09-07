# https://leetcode.com/problems/accounts-merge/
# https://raw.githubusercontent.com/Kohdz/LeetcodeImages/master/721_01.png?token=AD3LTZ2D546523QI2HLYIWK7KZBMI

from collections import defaultdict

def accountsMergeDFS(accounts):
    
    # user -> email: accounts
    # email -> user: emails
    # whether this user has been merged or not: visited
    
    visited = set()
    graph = defaultdict(list)
    output = []
    
    # Build up the graph.
    for i, account in enumerate(accounts):
        for j in range(1, len(account)):
            email = account[j]
            graph[email].append(i)
    
    # DFS code for traversing accounts.
    def dfs(i, emails):
        if i in visited:
            return
        visited.add(i)
        for j in range(1, len(accounts[i])):
            email = accounts[i][j]
            emails.add(email)
            for neighbor in graph[email]:
                dfs(neighbor, emails)
    
    # Perform DFS for accounts and add to results.
    for i, account in enumerate(accounts):
        if i in visited:
            continue
        name, emails = account[0], set()
        dfs(i, emails)
        output.append([name] + sorted(emails))
    return output


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(10001)]
    
    def find(self, x):
        while x != self.parent[x]:
            x = self.parent[x]
        return x
    
    def union(self, A, B):
        root_a = self.find(A)
        root_b = self.find(B)
        
        if root_a == root_b:
            return
        self.parent[root_a] = root_b


def accountsMergeUnionFind(accounts):
    uf = UnionFind(len(accounts))
    

    em_to_name = {}
    em_to_id = {}
    i = 0
    for acc in accounts:
        name = acc[0]
        for email in acc[1:]:
            em_to_name[email] = name
            if email not in em_to_id:
                em_to_id[email] = i
                i += 1
            uf.union(em_to_id[acc[1]], em_to_id[email])

    ans = defaultdict(list)
    for email in em_to_name:
        root = uf.find(em_to_id[email])
        ans[root].append(email)

    return [[em_to_name[v[0]]] + sorted(v) for v in ans.values()]
    
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"],
            ["John", "johnnybravo@mail.com"], 
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"], 
            ["Mary", "mary@mail.com"]]

# Output =  [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],
#            ["John", "johnnybravo@mail.com"], 
#            ["Mary", "mary@mail.com"]]

print(accountsMergeUnionFind(accounts))