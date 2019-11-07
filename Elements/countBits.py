def count_bits(x):
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits


x = 12  # 1100
print(count_bits(x))
# 1100 & 0001 # 0
# 0110 & 0001 # 0
# 0011 & 0001 # 1
# 0001 & 0001 # 1
