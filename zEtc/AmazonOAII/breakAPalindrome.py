'''
The smallest lexicographical order is an order relation where string s is smaller than t, given the first character of s (s[0]) is smaller than the first character of 
t (t[0]), or in case they are equivalent, the second character, and so on...
So aaabbb is smaller than aaac because although the first three characters are equal, the fourth character b is smaller than the fourth character c.
Out of all lowercase English letters, a has the lowest lexicographic value.
Therefore we should try and replace the first possible non-a character with an a.
If we exit the for loop without finding any non-a characters up until half of the string, we replace the final character with a b, to make sure it is the 
lexicographically smallest string that breaks the palindrome.
Replacing the first character with b would make it lexicographically bigger than the original string, which has all as up until the midpoint (where the loop stops).


If the input is invalid or the length of the string is 1 return an empty string.
For every char in the left half of the string:
  if the char is not 'a':
    return an identical string with that char flipped to 'a'
At this point the loop has broken so every character in our string is an 'a' other than potentially the middle char in an odd length string which will 
never break a palindrome.
return an identical string with the last char flipped to 'b'
'''


def breakPalindrome(palindrome):
    # The string is either empty or just one letter (in which case it's always a palindrome).
    if len(palindrome) < 2:
        return ''
    
    # Only need to iterate up to half of the string, since it's a palindrome.
    for i in range(len(palindrome) // 2):
        # Replace the first non-a character with an a.
        if palindrome[i] != 'a':
            return palindrome[:i] + 'a' + palindrome[i + 1:]
        
    # The lexicographically lowest string is where the last letter is replaced by b. 
    return palindrome[:len(palindrome) - 1] + 'b'