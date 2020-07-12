# https://leetcode.com/problems/binary-tree-right-side-view/

def rightSideViewDFS(root):
    def dfs(node, level):
        if not node:
            return
        
        if len(output) == level:
            output.append(node.val)
        
        # the key is traversing from right to left. 
        dfs(node.right, level+1)
        dfs(node.left, level+1)
        
    output = []
    dfs(root, 0)
    return output

def rightSideViewBFS(root):
    if not root:
        return []

    # BFS, add the node at the end
    # of the level
    queue = [root]
    output = []

    while queue:
        output.append(queue[-1].val)
        for _ in range(len(queue)):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return output