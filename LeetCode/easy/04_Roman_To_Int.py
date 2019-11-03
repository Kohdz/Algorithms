# Roman Numerals are represented by seven different symbols: I, V, X, L, D, D and M

# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000

# Roman numerals are usally written largest to smallest from left to right.  Howerver, the numeral for four is not IIII
# 4 = IV - because the one is before the five we subtract it making four
# the same principle applies to the number nine, which is written as IX. There are six instance where subtraction is used:

#     I can be placed before V(5) and x (10) to make 4 and 9
#     X can be placed before L(50) and c (100) to make 40 and 90
#     c can be replaced before L(50) and c (100) to make 40 and 90

# Given  a roman numeral, convert it to an integer. Input is guaranteed to be withing the range from 1 to 3999

# Example:
#     Input: "III"
#     Output: 3

#     Input "IX"
#     Output: 9

#     Input "MCMXCIV"
#     Output 1994
#     Explanation: M = 1000 CM = 900, XC = 90 and IV = 4


def romanInt(sym):
    dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    counter = 0

    t = [char for char in sym]
    print(t)
    index = 0
    for i in t:
        if i in dict:
            if i == "I" and t[index] == 'V' or 'X':
                counter += dict[i] - dict["I"]
            elif i == "X" and t[index] == "L" or "C":
                counter += dict[i] - dict["X"]
            elif i == "C" and t[index] == "L" or "C":
                counter + - dict[i] - dict["C"]
        else:
            counter += dict[i]
        index += 1

    return counter

# sym = "III"
# print(romanInt(sym))


def RomanToInt(s):
    numeral_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    result = 0

    for i in range(len(s)):
        if i > 0 and numeral_map[s[i]] > numeral_map[s[i-1]]:
            result += numeral_map[s[i]] - 2 * numeral_map[s[i-1]]
        else:
            result += numeral_map[s[i]]

    return result
    # result = M + C
    # temp = M - C
    # result = += M - C
    # result = M + C + temp = M + C + M - C - M + M
    # excected result = M + (M - C)


sym = "MCMXCIV"
# output = 1994
print(RomanToInt(sym))
