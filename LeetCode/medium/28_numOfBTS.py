# https://leetcode.com/problems/unique-binary-search-trees/


# Basically you have a  BST. Important to note becasue you can
# only attach a node that is smaller than it on the left
#  and only attach a node that is bigger than it on the right
# and since we will be repeating steps, i.e T(n) = 4 
# is basically T(4) = T(3) + T(2) + T(1)
#  we are caching information


# Time O(n^2) | Space O(n)

def numTrees(n):

    # numTree[4] = numTree[0] * numTree[3] +
    #              numTree[1] * numTree[2]
    #              numTree[2] * numTree[1] + 
    #              numTree[3] * numTree[1]

    numTree = [1] * (n + 1)

    # 0 node = 1 tree
    # 1 node = 1 tree
    for nodes in range(2, n + 1):
        total = 0

        for root in range(1, nodes + 1):
            left = root - 1
            right = nodes - root
            total += numTree[left] * numTree[right]
        numTree[nodes] = total
    return numTree[n]


n = 3
n2 = 5 
n3 = 10
print(numTrees(n) == 5)
print(numTrees(n2) == 42)
print(numTrees(n3) == 16796)