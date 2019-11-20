# https://leetcode.com/problems/intersection-of-two-arrays/

# Given two arrays, write a function to compute their intersection.

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Note:

# Each element in the result must be unique.
# The result can be in any order.


def set_interaction(set1, set2):
    return [x for x in set1 if x in set2]


# time O (n + m) where n and m are arrays lenght;  O (n) time used to
# convert to num1 sets. O (m) time used to convert num2 and contains/in operation (1)
#  space  O(m + n)
def interTwoSets(num1, num2):

    # sets can be used to solve problem in linear time
    #  sets get rid of repearting values
    #  sets order it and print out the intersect

    print("num1: ", num1)
    print("num2: ", num2)
    set1 = set(num1)
    set2 = set(num2)
    print("set1: ", set1)
    print("set2: ", set2)

    if len(set1) < len(set2):
        return set_interaction(set1, set2)
    else:
        return set_interaction(set2, set1)


nums1 = [3, 2, 1, 1]
nums2 = [1]

# nums1 = [4, 9, 5]
# nums2 = [9, 4, 9, 8, 4]
print(interTwoSets(nums1, nums2))


# time avg(n + m) bad(n x m) | space bad(n + m)
def interBuildIn(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    return list(set2 & set1)


print(interBuildIn(nums1, nums2))
