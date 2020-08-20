# https://leetcode.com/problems/longest-repeating-character-replacement/
# https://leetcode.com/problems/longest-repeating-character-replacement/discuss/91301/Awesome-python-solution

from collections import Counter

def characterReplacement(s, k):

    # Time: O(n)
    # Space: O(1)
    
    # We use a window ranging from index start to end
    # We only look in characters inside this window and keep track of their counts
    # We can allow up to K chars that are not the most frequent char in our window
    
    window_counts  = Counter()
    left = longest_window  = 0
    
    for right in range(len(s)):
            # at each loop, end is shifted to the right
        window_counts [s[right]] += 1
        
        # we shift start to the right only if we ran out of replacements
        # we ran out of replacements if (CHARS that are not the most frequent in current window) > k
        # (end - start + 1) is length of our window, because our window range is INCLUSIVE of both ends
        if right - left + 1 - window_counts.most_common(1)[0][1] > k:
            # since our window will be shifted, we subtract the character that we are shifting away from by 1
            # because it will no longer be in the new window                
            
            window_counts [s[left]] -= 1
            left += 1 # now shift our window
        
        # at each window, simply update res if our current window is larger
        longest_window  = max(longest_window , right - left + 1)
    
    return longest_window 

k = 1
s = "AABABBA"
print(characterReplacement(s, k))