from collections import defaultdict

def gardenNoAdj(N, paths):
    
    # Translate paths into adjacency list
    # create a graph to show the path between the gardens
    graph = defaultdict(list)
    for src, dst in paths:
        graph[src].append(dst)
        graph[dst].append(src)
        
    colored = defaultdict()
    
    def dfs(G, V, colored):
        colors = [1, 2, 3, 4]
        for nei in G[V]:
            if nei in colored:
                if colored[nei] in colors:
                    colors.remove(colored[nei])
        colored[V] = colors[0]
        
    # loop for all the gardens
    #   for each garden, remove neighbors' plants from its available choices;
    #   plant any one available.
    for V in range(1, N + 1):
        dfs(graph, V, colored)
        
    output = []
    for V in range(len(colored)):
        output.append(colored[V + 1])
        
    return output
        
N = 3
paths = [[1,2],[2,3],[3,1]]
# Output: [1,2,3]

N2 = 4 
paths2 = [[1,2],[3,4]]
# Output: [1,2,1,2]

N3 = 4
paths3 = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
# Output: [1,2,3,4]

print(gardenNoAdj(N, paths))
print(gardenNoAdj(N2, paths2))
print(gardenNoAdj(N3, paths3))