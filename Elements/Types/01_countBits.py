def count_bits(x):
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits


# print(4 and 8)
# print(4 & 8)


# 1100 & 0001 # 0
# 0110 & 0001 # 0
# 0011 & 0001 # 1
# 0001 & 0001 # 1
# and correctly return 2. By right shifting, you count the bits from right to left until
#  the last shift results in 0000 and breaks the loop


a = 15
print(bin(a))
print(count_bits(a))


