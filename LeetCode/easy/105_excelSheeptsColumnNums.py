# https://leetcode.com/problems/excel-sheet-column-number/
# https://www.youtube.com/watch?v=g-l4UpF62x0

def titleToNumber(s):
    
    result = 0
    
    for char in s:
        d = ord(char) - ord('A') + 1
        result = result*26 + d
        
    return result

s = 'A'
print(titleToNumber(s))