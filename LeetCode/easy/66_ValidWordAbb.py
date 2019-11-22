# https://leetcode.com/problems/valid-word-abbreviation/

# Given a non-empty string 'a' and an abbervation 'abbr',
# return whether the string matches the given abbervation

# a string such as "word" contains only the following valid
# abberations:

# ["word", "lord", "wlrd", "wold", "wor1", "2rd", "w2d",
# "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]

# Notice that only the above abberivations are valid abbervations of
# the string "word". Any other string is not a valid abberviation of
# "word"

# Note:
# Assume "a" contains only lowercase letters and "abbr" contains only
# lowercase letters and digits

# Example 1:
#     Given s = "internationalization", abbr = "il2iz4n"
#     Return True

# Example 2:
#     Given s = "apple", abbr = "a2e"
#     Return False


def validWordAbbrevation(word, abbr):
    i, j = 0, 0
    while i < len(abbr):
        if j >= len(word):
            return False
        if not abbr[i].isdigit():
            if abbr[i] != word[j]:
                return False
            i += 1
            j += 1
        else:
            if abbr[i] == '0':
                return False
            n = ''
            while i < len(abbr) and abbr[i].isdigit():
                n += abbr[i]
                i += 1
            j += int(n)
    return j == len(word)


s1 = "internationalization"
abbr1 = "i12iz4n"
# Return True

s2 = "apple"
abbr = "a2e"
# Return False

print(validWordAbbrevation(s1, abbr1))
