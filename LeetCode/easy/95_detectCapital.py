# https://leetcode.com/problems/detect-capital/

# Time O(n) | Space O(1)

def detectCapitalUse(word):
        
    if word.isupper():
        return True
    elif word.islower():
        return True
    elif word[0].isupper() and word[1:].islower():
        return True 
    else:
        return False
    
words = ["USA", "FlaG", "Usa", "UsA", "usA", "uAs"]
bool =  [True, False, True, False, False, False]

for i in range(len(words)):
    print(detectCapitalUse(words[i]) == bool[i])

