from collections import defaultdict


def singleNumber_BruteForce(nums):
    """
    :type nums: List[int]
    :rtype: int

    Time O (n^2) | space O (n)
    """
    no_duplicate_list = []
    for i in nums:
        if i not in no_duplicate_list:
            no_duplicate_list.append(i)
        else:
            no_duplicate_list.remove(i)
    return no_duplicate_list.pop()


def singleNumber_HashTable(nums):
    """
    Time O (n) | Space O (n)
    """
    hash_table = defaultdict(int)
    for i in nums:
        hash_table[i] += 1

    for i in hash_table:
        if hash_table[i] == 1:
            return i


def singleNumber_Binaty(nums):
    """
    :type nums: List[int]
    :rtype: int

    Time O (n) | Space O (1)
    """
    a = 0
    for i in nums:
        a ^= i
    return a
