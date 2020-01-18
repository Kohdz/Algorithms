# https://stackoverflow.com/questions/59531070/compute-x-y-without-arithmetical-operators

# below is the long division for binary numbers
# if we divide x by y, we ask, "how many times does y
# fit into x if we add as many zeros to it as possible"
# Adding n zeros to y is equivalent to multiplying with 2^n
# or shifting left by n
# example 10 / 3
#  answer is 3
# 2^n * y = 2^0 * y = 3 (n = 0 bc 3 fits into 10 without any 0)
#  also y << n = y << n = 3 (we arrive at 3 both ways)


def divide(x, y):

    # 32 to is added to by  because our result
    # is >= 2^33 (it is 32 bit numbers)

    result, power = 0, 32
    y_power = y << power

    print("power: ", power)
    print("y_power: ", y_power)
    print("")
    # we will stop if the difference, y, is smaller than x
    # and it is therefore impossible for 2^power * y to fit into x

    while x >= y:
        print("x: ", bin(x))
        print("y: ", bin(y))
        print("")
        # this loop tests if y_power already fits into x
        # and if not, will "move it one digit to the right"

        while y_power > x:
            y_power >>= 1
            power -= 1
            print("y_power: ", bin(y_power))
            print("power: ", bin(power))

        # after inner loop finishes, it will write the
        # number of how many times y shifted left fits into x
        # to the result.  As in binay numbers this can be zero
        # or one and the inner loop skipped all zeros, this must be1
        result += 1 << power
        print("result: ", result)
        print("")

        # simmilar to long division, we now need to subtract this
        # multiple of the divisor y, from the dividend and continue with
        # the result
        x -= y_power

    return result


print(divide(10, 3))
