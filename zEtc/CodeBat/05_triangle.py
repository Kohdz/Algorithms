# We have triangle made of blocks. The topmost row has 1 block, the next row down has 2 blocks,
# the next row has 3 blocks, and so on. Compute recursively (no loops or multiplication) the total
#  number of blocks in such a triangle with the given number of rows.


# triangle(0) → 0
# triangle(1) → 1
# triangle(2) → 3

def triangle(n):

    if n <= 1:
        return n

    return 1 + triangle(n-1)


rows = 0  # 0
rows2 = 1  # 1
rows3 = 3  # 3

print(triangle(rows))
print(triangle(rows2))
print(triangle(rows3))
