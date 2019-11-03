# Determine whether an integer is a palindrome. An integer is a palindrome when
# it reads the same backwords as fordwards

# example 1:
#     Input: 121
#     Output: True

# example 2:
#     Input: -121
#     Output: False


def palNum(num):
    a = abs(num)
    pal = True
    rev = 0

    while a > 0:
        temp = a % 10
        rev = rev * 10 + temp
        a = a // 10

    print(rev)
    if num != rev:
        pal = False

    return pal


num1 = 121

print(palNum(num1))
