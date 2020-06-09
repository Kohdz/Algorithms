# https://leetcode.com/problems/longest-substring-without-repeating-characters


def lengthOfLongestSubstring(s):
    length, start = 0, 0
    seen = {}
    for idx, c in enumerate(s):
        if c in seen and start <= seen[c]:
            start = seen[c] + 1
        length = max(length, idx-start+1)
        seen[c] = idx
    return length



str1 = "abcabcbb"
# Output: 3 

str2 = "bbbbb"
# Output: 1

str3 = "pwwkew"
# Output: 3

print(lengthOfLongestSubstring(str1) == 3)
print(lengthOfLongestSubstring(str2) == 1)
print(lengthOfLongestSubstring(str3) == 3)