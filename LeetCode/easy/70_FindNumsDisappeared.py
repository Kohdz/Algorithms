# Find All Numbers Disappeared in an Array


# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array),
#  some elements appear twice and others appear once.

# Find all the elements of [1, n] inclusive that do not appear in this array.

# Could you do it without extra space and in O(n) runtime?
#  You may assume the returned list does not count as extra space.

# Example:
# Input: [4,3,2,7,8,2,3,1]

# Output: [5,6]


def findDisappearedNumbers(nums):

    # set is unordered collection of items
    # each element is unique (no dups) and
    # must be immutable  (cannot be changed)
    # howerver the set itself is mutable
    # we can add or remove from it

    # sets can be used to perfrom mathmaetical set
    # operations like union, intersection, symetric difference

    len_arr = len(nums) + 1
    a = set([i for i in range(1, len_arr)])
    b = set(nums)
    return (a-b)


nums = [4, 3, 2, 7, 8, 2, 3, 1]  # [5, 6]
print(findDisappearedNumbers(nums))
