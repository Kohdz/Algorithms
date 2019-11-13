# Write a Python program to calculate the sum of a list of numbers


# Write a Python program to converting an Integer to a string in any base


def to_string(num, base):
    conver_tString = "0123456789ABCDEF"
    if num < base:
        return conver_tString[num]
    else:
        return to_string(num//base, base) + conver_tString[num % base]


print(to_string(2835, 16))
