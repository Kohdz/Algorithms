

# assuming y > x
# mod x by y
# keep doing this until y = 0 and then return x
# geometrically, imagine a rectangle
# you are trying to cut the rectangle into squares
# the length of the smallest square is the GCD

def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)


print(gcd(156, 36))
