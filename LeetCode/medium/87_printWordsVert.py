# https://leetcode.com/problems/print-words-vertically/


def printVertically(s):
    
    # split string into a list of words
    s = s.split()
    
    # finds the length of each word and create a list of them
    s_len = [len(i) for i in s]
    
    # finds the longest word in list of lengths
    max_len_word = max(s_len)
    
    # creates a list of empty string of the correct size for the result
    res = max(s_len) * [""]
    
    # j is the index of each word in the result
    for j in range(max(s_len)):
        
        # i is the index of each char in the initial string s
        for i in range(len(s)):
            
            # adds a char to the result if it exist if not it adds whitespace
            if s_len[i] <= j:
                res[j] += ' '
            else:
                res[j] += s[i][j]
                
        # checks for white space at the end of a word
        if res[j][-1] == ' ':
            res[j] = res[j].rstrip()
    
    # result
    return res

s = "HOW ARE YOU"
print(printVertically(s))