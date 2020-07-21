# https://leetcode.com/problems/house-robber-iii/

# On every node we got two option, to rob or not to rob

# To rob this node, then we cannot rob our left and right child, so the max value would be the total of
    #    value of this node
    #   the max value from left child, when we not rob the left child
    #   the max value from right child, when we not rob the right child

# Not to rob this node, means that we can either rob or not rob our left and right child, so the max value would be the total of
    #   0, because we choose not to rob this node
    #   the max of rob the left child and not rob the left child
    #   the max of rob the right child and not rob the right child


# DFS + DP
def rob(root):
    def superrob(node):
        # returns tuple of size two (now, later)
        # now: max money earned if input node is robbed
        # later: max money earned if input node is not robbed
        
        # base case
        if not node: return (0, 0)
        
        # get values
        left, right = superrob(node.left), superrob(node.right)
        
        # rob now
        now = node.val + left[1] + right[1]
        
        # rob later
        later = max(left) + max(right)
        
        return (now, later)
        
    return max(superrob(root))


# DFS memecache
def robCache(root):

    # Recurrence relation: dp[i] = max(root.val + dp[i -2], dp[i - 1])
    mem = {}
    def dp(node, allow):
        if not node: return 0
        key = (node, allow)
        if key in mem:
            return mem[key]
        ans = dp(node.left, True) + dp(node.right, True)
        if allow:
            ans = max(ans, node.val + dp(node.left, False) + dp(node.right, False))
        mem[key] = ans
        return ans
    
    
    return dp(root, True)