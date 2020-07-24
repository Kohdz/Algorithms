# https://leetcode.com/problems/number-of-lines-to-write-string/


def numberOfLinesI(widths, S):
    
    units = 0
    lines = 1
    for char in S:
        units += widths[ord(char) - ord("a")]
        
        # move to a new line
        if units > 100:
            units = widths[ord(char) - ord("a")]
            lines += 1
        
    return [lines, units]
        
        

def numberOfLinesII(widths, S):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    line = 1
    width = 0
    for letter in S:
        width += widths[alphabets.index(letter)]
        if width > 100:
            line += 1
            width = widths[alphabets.index(letter)]
    return [line,width]

widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "abcdefghijklmnopqrstuvwxyz"
# Output: [3, 60]
# Explanation: 
# All letters have the same length of 10. To write all 26 letters,
# we need two full lines and one line with 60 units.

print(numberOfLinesI(widths, S))