# https://leetcode.com/problems/majority-element/


# Given an array of size n, find the majority element. The majority element
# is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

# Example 1:
# Input: [3,2,3]
# Output: 3

# Example 2:
# Input: [2,2,1,1,1,2,2]
# Output: 2

import collections
import random


def majorityElement(nums):
    dict = {}
    majLimit = len(nums) // 2

    for i in range(len(nums)):
        print(i)
        print(dict)
        if nums[i] not in dict:
            dict[nums[i]] = 0
        else:
            dict[nums[i]] += 1

    print(dict)
    for key, value in dict.items():
        if value >= majLimit:
            return key


nums1 = [3, 2, 3]  # 3
nums2 = [2, 2, 1, 1, 1, 2, 2]  # 2
print(majorityElement(nums2))


# time (n^2) | space O (1)
def majorityElementBrute(nums):
    majority_count = len(nums)//2
    for num in nums:
        count = sum(1 for elem in nums if elem == num)
        if count > majorityElement:
            return num


# time (n) | space (n)
def majorityElementHashMap(nums):
    # we iterate over nums and make a constant time HashMap insertion on each iteration
    # that is what contributes to(n) time complexity
    # hashmap can contain n - [n/2] associates so it occupies(n) space
    # this is because an arbitrary array of lenght n can contain n distict values
    # but nums is guaranteed to contain a majoiry element which will occupy(at min)
    # [n/2] + 1 array indices; thus n - ([n/2]+1) indices can be occupied by distict
    # non-majority element (plus 1 for the majority element itself) leaving us with
    # at most n - n/2 distinct elements

    counts = collections.Counter(nums)
    return max(counts.keys(), key=counts.get)


# time(n lgn) | space(1) pr(n)
def majorityElementSorting(nums):
    # if elements are sorted in monotonically increasing(or decreasing) order,
    # the majority of elements can be found at index[n/2](and [n/2] + 1) even if n is even

    # no matter what the the value the majority element has in relation to the rest of the array,
    # returning the value at n/2 will never be wrong

    nums.sort()
    return nums[len(nums)//2]


# time(1) | space(1)
def majorityElementRand(nums):

    # time complexity is can in theory be infinite
    # expected is far better than linear
    #  if we take the limit, we see that it converges at 2

    # because more then[n/2] array indices are occupied by the majority element, a random
    # array index is likely to contain the majority element

    # just select a random index and check wheter its value is the most element
    # if it is return it, else try again

    majoirty_count = len(nums) // 2

    while True:
        candiate = random.choice(nums)
        if sum(1 for elem in nums if elem == candiate) > majoirty_count:
            return candiate


# time (n lgn) | space (lgn)
def majorityElementRec(nums, lo=0, hi=None):
    # if we know the majoity element in the left and right halves of an array
    # we can determine which is the global majoirty element in linear time

    def DivAndConq(lo, hi):

        # base case; the only element in an array of size 1 is the majority element
        if lo == hi:
            return nums[lo]

        # recurse on left and right halves of this slice
        mid = (hi-lo) // + lo
        left = DivAndConq(lo, mid)
        right = DivAndConq(mid+1, hi)

        # if the two halves agree on the majority element, return it
        if left == right:
            return left

        # otherwise, count each element and return the "winner"
        left_count = sum(1 for i in range(lo, hi+1) if nums[i] == left)
        right_count = sum(1 for i in range(lo, hi+1) if nums[i] == right)

        return left if left_count > right_count else right

    return DivAndConq(0, len(nums)-1)

# time (n) | space (1)


def majorityElementBoyer(nums):

    # Boyer-Moore perfomrs constant work exactly n time
    # so the algorithms run in linear time

    # basically, if count is 0, initialize on the next candiate
    #  else just subtract 1 if it is another canadiate
    #  but add one if it is the same canidate
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate
