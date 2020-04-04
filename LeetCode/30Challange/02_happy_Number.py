size = 0


def isHappy(n):
    size = 0
    s = set()
    while n != 1:
        if n in s:
            return False
        s.add(n)
        n = sum([int(i) ** 2 for i in str(n)])
    return True


n = 19
print(isHappy(n))
