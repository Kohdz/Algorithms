# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

import collections


def maxDepth(root):

    if not root:
        return 0

    
    depth = 0
    queue = collections.deque([root])

    while queue:

        level = []
        u = queue.popleft()

        for _ in range(len(queue)):

            for child in u.children:
                level.append(child)
        
        depth += 1

        queue.extend(level)

    return depth