# https://leetcode.com/problems/valid-palindrome/



#Two Methods
def isPalindromeTwoPointers(s):
    
    left, right = 0, len(s)-1
    
    while left < right:
        
        # skip non-alphanumeric characters on left hand side
        while not s[left].isalnum() and left < right:
            left += 1
        
        # skip non-alphanumeric characters on right hand side
        while not s[right].isalnum() and left <right:
            right -=1
        
        # compare
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1

    return True


def isPalindromeStringMethods(s):

    letters = [ char.lower() for char in s if char.isalnum() ]    
    return letters == letters[::-1]

s = "A man, a plan, a canal: Panama"
print(isPalindromeTwoPointers(s))