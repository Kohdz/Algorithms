# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Given a binary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest path from
#  the root node down to the farthest leaf node.

# Note: A leaf is a node with no children.

# Example:

# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its depth = 3.


def BinaryTree(r):
    	return [r, [], []]

def insertLeft(root,newBranch):
	t = root.pop(1)
	if len(t) > 1:
		root.insert(1,[newBranch,t,[]])
	else:
		root.insert(1,[newBranch, [], []])
	return root

def insertRight(root,newBranch):
	t = root.pop(2)
	if len(t) > 1:
		root.insert(2,[newBranch,[],t])
	else:
		root.insert(2,[newBranch,[],[]])
	return root

def getRootVal(root):
	return root[0]

def setRootVal(root,newVal):
	root[0] = newVal

def getLeftChild(root):
	return root[1]

def getRightChild(root):
	return root[2]

#     3
#    / \
#   9  20
#     /  \
#    15   7




b = BinaryTree('a')
# Build up the left side of this tree
insertLeft(b,'b')
insertRight(getLeftChild(b),'d')

# Build up the right side of this tree
insertRight(b,'c')
insertLeft(getRightChild(b),'e')
insertRight(getRightChild(b),'f')

print(getRightChild(b))
def maxDepth(node):

    if node is None:
        return 0
    else:
        return max(maxDepth(node.left), maxDepth(node.right)) + 1

