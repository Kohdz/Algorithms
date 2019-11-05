# https://leetcode.com/problems/longest-common-prefix/
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


# strs = ["flower", "flow", "flight"]
# # Output: "fl"


# def longestCommonPrefix1(strs):

#     if not strs:
#         return ""

#     # i
#     # strs[0][i] ?= strs[1][i]
#     for i in range(len(strs[0])):
#         for string in strs[1:]:
#             print(string)
#             print(string[i])
#             print(strs[0][i])
#             print(" ")
#             if i >= len(string) or string[i] != strs[0][i]:
#                 return strs[0][:i]

#     return strs[0]


# print(longestCommonPrefix1(strs))


# def longestCommonPrefix2(strs):

#     result = ""
#     i = 0

#     while True:
#         try:
#             sets = set(string[i] for string in strs)
#             if len(sets) == 1:
#                 result += sets.pop()
#                 i += 1
#             else:
#                 break
#         except Exception as e:
#             break

#     return result


# print(longestCommonPrefix2(strs))


strs = ["flower", "flow", "flight"]
