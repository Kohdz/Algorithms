def multiply(x, y):
    def add(a, b):
        running_sum, carryin, k, temp_a, temp_b = 0, 0, 1, a, b

        while temp_a or temp_b:
            ak, bk = a & k, b & k
            carryout = (ak & bk) | (ak & carryin) | (bk & carryin)
            running_sum |= ak ^ bk ^ carryin
            carryin, k, temp_b, temp_b = (
                carryout << 1, k << 1, temp_a >> 1, temp_b >> 1)

        return running_sum | carryin

    running_sum = 0
    while x:  # Examines each bit of x
        if x & 1:
            running_sum = add(running_sum, y)
        x, y = x >> 1, y << 1

    return running_sum


print(multiply(2, 2))
