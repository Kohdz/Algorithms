# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

# Amazon Music Pair



from collections import defaultdict

# Time O(n) | Space O(1)
# because the size of the array `remainders` is fixed with 60

def getSongPairCount(songs):
        pairCounts = defaultdict(int)
        count = 0
        for song in enumerate(songs):
            if (60-(song%60))%60 in pairCounts:
                count+=pairCounts[(60-(song%60))%60]
            pairCounts[(song%60)] +=1
        return count