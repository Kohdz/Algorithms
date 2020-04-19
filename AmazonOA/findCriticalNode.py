# https://leetcode.com/discuss/interview-question/436073/Amazon-or-OA-2019-or-Critical-Routers/392473


def FindCriticalNodes(numEdges, numNodes, edges):

    # Get all the node
    nodes = []
    for i in range(numEdges):
        # Get nodes
        if edges[i][0] not in nodes:
            nodes.append(edges[i][0])

        if edges[i][1] not in nodes:
            nodes.append(edges[i][1])

    # Get all the neighbours
    neighbours = {node: [] for node in nodes}
    for i in range(numEdges):
        # Get neighbours
        neighbours[edges[i][0]].append(edges[i][1])
        neighbours[edges[i][1]].append(edges[i][0])

    def dfs(parent, seen):
        nonlocal neighbours
        #print("Visiting node {}".format(parent))

        # Mark the parent as explored
        seen[parent] = 1

        # Get all the neighbours from parent
        neig = neighbours[parent]

        # Iterate all the neighbours
        for i in range(len(neig)):
            # return if this node was exlored
            if seen[neig[i]] == 1:
                continue

            # DFS
            dfs(neig[i], seen)

    # Loop over all the nodes
    output = []
    for i in range(numNodes):
        explored = {node: 0 for node in nodes}

        # Mark the cutting point as explored as we
        # don't wanna explore this point
        explored[nodes[i]] = 1

        # DFS
        # Traverse from 0 every time
        total_visited = 1
        dfs(nodes[0], explored)

        print("Node {}: Explores {} nodes.".format(
            nodes[i], sum(explored.values())))
        # If all nodes are explored, it means it's not articulate point
        if(sum(explored.values()) < numNodes):
            output.append(nodes[i])

    print(neighbours, nodes)
    print(output)


numNodes, numEdges = 7, 7
edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
FindCriticalNodes(numNodes, numEdges, edges)
