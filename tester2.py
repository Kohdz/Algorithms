# 6.  Write a program which takes as input a sorted array and updates it so that all duplicates have been removed and the
#  remaining elements have been shifted left to fill the emptied indices.  Return the number of valid elements.  Many
# languages have library functions for performing this operation -- you cannot use these functions


def delete_dup(A):

    # since it is sorted, we want to be able to abuse that fact
    # so we go i and i + 1;
    # compate the nums
    # if they are not the same, keep moving
    # return endicies, meansing 6
    # if they are same swap, then ending indixes

    pass


A = [2, 3, 5, 5, 7, 11, 11, 13]  # 6 elements
print(delete_dup(A))
# 7. Write a program that takes an array denoting the daily stock price, and returning the maximum profit that could be made
# by buying and then selling one share of that stock.  There is no need to buy if no profit is possible

#       A = [310, 315. 275, 295, 260, 270, 290, 230, 255, 250] #30

# 8. Write a program that computes the maximum profit that can be made by buying and selling a share at most twice. The second
# buy must be made on another date after the first sale.

#       A = [12, 11, 13, 9, 12, 8, 14, 13, 15] #10

# 9. Write a program that takes an array A of n numbers, and rearranges A's elements to get a new array B having the property that
# B[0] <= B[1] >= B[2] <= B[3] >= B[4] <= B[5] >= ...

#       A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 10.  A natural number is called a prime if it has a bigger than 1 and has no divisors other than 1 and itself. For example, if the
#  input is 18, you should return [2, 3, 5, 7, 11, 13, 17]

#       n = 18 #[2, 3, 5, 7, 11, 13, 17]
