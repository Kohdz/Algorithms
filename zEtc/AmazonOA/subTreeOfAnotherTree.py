
def isSame(s, t):
    if s is None and t is None:
        return True
    if s is None or t is None:
        return False
    if s.val != t.val:
        return False

    return isSame(s.left, t.left) and isSame(s.right, t.right)


def traverse(s, t):
    if s is None:
        return False

    return isSame(s, t) or traverse(s.left, t) or traverse(s.right, t)


# traverse(s, t)
