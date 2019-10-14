# Determine whether an integer is a palindrome. An integer is a palindrome when
# it reads the same backwords as fordwards

# example 1:
#     Input: 121
#     Output: True

# example 2:
#     Input: -121
#     Output: False


def isPal(num):

    a = abs(num)
    temp = 0
    while a > 0:
        mod = a % 10

        temp = temp* 10  + mod
        a = a // 10

    if


    return temp


num = 121
print(isPal(num))