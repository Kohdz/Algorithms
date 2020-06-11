# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

import collections

# BFS + Hash Set O(n) time and space
def findTarget(root, k):



    queue = collections.deque([root])
    seen = set()

    while queue:

        u = queue.popleft()

        if k - u.val in seen:
            return True
        else:
            seen.add(u.val)
        
        if u.left:
            queue.append(u.left)

        if u.right:
            queue.append(u.right)

    return False

