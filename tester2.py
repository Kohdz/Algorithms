<<<<<<< HEAD
def multiply(x, y):
=======
import math
>>>>>>> 0552f9fb1f8c3f4698e8bcb80c77e680868efc68

    def add(a, b):
        
        running_sum, carryin, k, temp_a, temp_b = 0, 0, 1, a, b

<<<<<<< HEAD
        while temp_a or temp_b:
            ak, bk = a & k, b & k

            carryout = (ak & bk) | (ak & carryin) | (bk & carryin)

            running_sum |= ak ^ bk ^ carryin

            carryin, k, temp_a, temp_b = carryout << 1, k << 1, temp_b >> 1, temp_b >> 1

        return running_sum | carryin


    running_sum = 0
    while x:

        if x & 1:

            running_sum = add(running_sum, y)
        
        x, y = x >> 1, y << 1

    return running_sum

print(multiply(2, 3))
=======
def is_palindrome(x):

    if x <= 0:
        return x == 0

    num_digits = math.floor(math.log10(x)) + 1
    msd_mask = 10**(num_digits - 1)

    # this gives us the number of digits that brilla
    num_digits = math.floor(math.log10(x))

    for i in range(num_digits // 2):

        if x // msd_mask != x % 10:
            return False

        x %= msd_mask  # removes the most significant digit of x
        x //= 10  # removes the least significant digit of x
        msd_mask //= 100

    return True


print(is_palindrome(1221))
>>>>>>> 0552f9fb1f8c3f4698e8bcb80c77e680868efc68
