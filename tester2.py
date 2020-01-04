# 9.  Write a program that takea an integer and determines if that integer representation as a decimal string
# is a palindrome.  For example 121 is is a palindrome; 7 is a palindrome; -1 is not
import math


def isPal(x):
    # we check first digit
    # we check last digit
    # if not equal then return fals
    # else teturn true
    # negative numbers are not pals

    # in more detail
    # we take last digit my using mod
    # we get first digit by usisng mask and log
    # so import math
    # them we update the mask with div 2 becasue we reduce diigt by 2 every time

    if x <= 0:
        return x == 0

    num_digits = math.floor(math.log10(x)) + 1
    msd_mask = 10**(num_digits - 1)

    for i in range(num_digits // 2):

        if x // msd_mask != x % 10:
            return False

        # how do we update

        x %= msd_mask  # removes most sig dig
        x //= 10  # removes lest sig dig
        msd_mask //= 100  # removes 2 00 from mask

    return True


x = 1221
print(isPal(x))
