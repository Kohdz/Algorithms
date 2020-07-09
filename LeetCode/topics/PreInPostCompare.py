# Comparision of Pre/In/Post Order Iterative Solution


def preOrder(root):
    stack,res=[root],[]
    while stack:
        if isinstance(stack[-1],int):
            res.append(stack.pop())
            continue
        node=stack.pop()
        if not node:
            continue
        stack.extend([node.val, node.right, node.left])
    return res

def inOrder(root):
    stack,res=[root],[]
    while stack:
        if isinstance(stack[-1],int):
            res.append(stack.pop())
            continue
        node=stack.pop()
        if not node:
            continue
        stack.extend([node.right, node.val, node.left])
    return res

def postOrder(root):
    stack,res=[root],[]
    while stack:
        if isinstance(stack[-1],int):
            res.append(stack.pop())
            continue
        node=stack.pop()
        if not node:
            continue
        stack.extend([node.right, node.left, node.val])
    return res