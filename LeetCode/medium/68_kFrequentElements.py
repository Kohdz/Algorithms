'''
Problem: https://leetcode.com/problems/top-k-frequent-elements/
Helpful Links:
    https://www.youtube.com/watch?v=hGK_5n81drs
    https://www.youtube.com/watch?v=aXJ-p3Qa4TY
    https://www.youtube.com/watch?v=BP7GCALO2v8
'''


import heapq
import random
from collections import Counter


def topKFrequent(nums, k):
    '''
    Time O (N log k) if k < N and O(N) in the partcular case N = k
    That ensures time complexity to be better than O (N log N)
    
    Space: O(N + K) to store the hash map with not more N elements
    # and a heap with k elements
    '''
    
    # O(1) time
    if k == len(nums):
        return nums 
    
    # 1. build hash map: character and how often it appears
    # O(N) time
    count = Counter(nums)
    
    # 2-3. build heap of top k frequent elements and
    # convert it into an output array
    # O(N log k) time
    return heapq.nlargest(k, count.keys(), key=count.get)


def topKFrequentQuickSelect(nums, k):
    '''
    Time O(N) in average case and O(N^2) in worst case
    In case of bad pivot, we end up doing (n -1) each time and
    not not (n/2)

    Space O(N) to store hash map and array of unique elements
    '''

    count = Counter(nums)
    unique = list(count.keys())
    
    def partition(left, right, pivot_index) -> int:
        pivot_frequency = count[unique[pivot_index]]
        # 1. move pivot to end
        unique[pivot_index], unique[right] = unique[right], unique[pivot_index]  
        
        # 2. move all less frequent elements to the left
        store_index = left
        for i in range(left, right):
            if count[unique[i]] < pivot_frequency:
                unique[store_index], unique[i] = unique[i], unique[store_index]
                store_index += 1

        # 3. move pivot to its final place
        unique[right], unique[store_index] = unique[store_index], unique[right]  
        
        return store_index
    
    def quickselect(left, right, k_smallest) -> None:
        """
        Sort a list within left..right till kth less frequent element
        takes its place. 
        """
        # base case: the list contains only one element
        if left == right: 
            return
        
        # select a random pivot_index
        pivot_index = random.randint(left, right)     
                        
        # find the pivot position in a sorted list   
        pivot_index = partition(left, right, pivot_index)
        
        # if the pivot is in its final sorted position
        if k_smallest == pivot_index:
            return 
        # go left
        elif k_smallest < pivot_index:
            quickselect(left, pivot_index - 1, k_smallest)
        # go right
        else:
            quickselect(pivot_index + 1, right, k_smallest)
    
    n = len(unique) 
    # kth top frequent element is (n - k)th less frequent.
    # Do a partial sort: from less frequent to the most frequent, till
    # (n - k)th less frequent element takes its place (n - k) in a sorted array. 
    # All element on the left are less frequent.
    # All the elements on the right are more frequent.  
    quickselect(0, n - 1, n - k)
    # Return top k frequent elements
    return unique[n - k:]


k = 2
nums = [1,1,1,2,2,3]
# Output: [1,2]

print(topKFrequent(nums, k))