# https://leetcode.com/problems/excel-sheet-column-title/

# Given a positive integer, return its corresponding column title as appear in an Excel sheet.

# For example:
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB
#     ...


def convertToTitle(n):

    result, num = "", n

    while num:
        result += chr((num-1) % 26 + ord('A'))
        num = (num-1) // 26

    return result[::-1]


def convertToTitle2(n):
    """
    :type n: int
    :rtype: str
    """
    dic = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = ''
    while n > 0:
        # n, rem = divmod(n-1, 26)
        n = n // 26
        rem = n % 26
        print("n", n)
        print("rem", rem)
        res = dic[rem] + res
    return res

# Input: 1
# Output: "A"

# Input: 28
# Output: "AB"


n1 = 1  # should return "A"
n4 = 26  # should return "Z"
n2 = 28  # should return "AB"
print(convertToTitle2(n2))
