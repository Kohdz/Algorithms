# https://leetcode.com/problems/letter-tile-possibilities





def numTilePossibilities(tiles):

    def perm(s, temp, ans):

        ans.add(temp)
        for i in range(len(s)):
            perm(s[:i]+s[i+1:], temp+s[i], ans)

    ans = set()
    perm(tiles, "", ans)
    return len(ans) - 1



tiles = "AAB"
# Output: 8
# Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

print(numTilePossibilities(tiles))