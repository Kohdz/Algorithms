size = 0


def isHappy(n):

    s = set()
    while n != 1:
        if n in s:
            return False
        s.add(n)
        n = sum([int(i) ** 2 for i in str(n)])
    return True


def calc_sum(n):
    result = n
    s = 0
    while result > 0:
        rem = result % 10
        s += rem ** 2
        result = result // 10
    return s


def isHappy2(n):
    seen = set()
    while n not in seen and n != 1:
        seen.add(n)
        n = calc_sum(n)
    return n == 1


n = 19
print(isHappy2(n))
