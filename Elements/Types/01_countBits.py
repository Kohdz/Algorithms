def count_bits(x):
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits


<<<<<<< HEAD:Elements/countBits.py
print(4 and 8)
print(4 & 8)


=======
x = 12  # 1100
print(count_bits(x))
>>>>>>> e76d3942b12bca3e2b8ff0e83ed04b4246b4823b:Elements/Types/01_countBits.py
# 1100 & 0001 # 0
# 0110 & 0001 # 0
# 0011 & 0001 # 1
# 0001 & 0001 # 1
<<<<<<< HEAD:Elements/countBits.py
# and correctly return 2. By right shifting, you count the bits from right to left until
#  the last shift results in 0000 and breaks the loop

=======
>>>>>>> e76d3942b12bca3e2b8ff0e83ed04b4246b4823b:Elements/Types/01_countBits.py
