# 1. Write A Program to count the number of bits set to 1

#       x = 12 # 1100

# 2. How would you compute the parity of a very large number of 64-bit words
# - Method 1
# - Method 2
# - Method 3

#       x = 12 # 1100

# 3. Swap Bits. Swap the i-index bit. Swap the first bit with the 6th bit

#       x = 0b01001001 #00001011

# 4. Write a program that takes a 64-th bit unsigned integer and returns the 64-bit unsigned
# integer consisting of the bits of the input in reverse order.  For example, the input is
# (1110000000000001), the output should be (1000000000000111).

#       x = 0b1110000000000001 #1000000000000111

# 5. Define the weight of a nonnegative integer x to be the number of bits that are set to 1
# in its binary representation.  For example, since 92 in base-2 equals (1011100), the weight
# of 92 is 4.  Write a program which takes as input a nonnegative integer x and returns a
# number y which is not equal to x, but has the same weight as x and their difference, |y - x|,
# is as small as possible.  You can assume x is not 0, or all 1s.  For example, if x = 6,
# you should return 5.  You can assume the integer fits in 64 bits.

#       x = 6 #5

#  6. Write a program that multiplies two nonnegative integers.  The only operators you are
#  allowed to use are
#     - assignment
#     - the bitwise operators >>, <<, |, &, ~, ^, and
#     - equality checks and Boolean combinations thereof

#       x = 3
#       y = 2

# 7. given two postive integers, compute their quotient, using only the addition, subtraction
# and shifting operators
# relate x/y to (x-y)/y

#       x = 10
#       y = 3

# 8. Write a program that takes a doube x and an integer y and returns x^y, You can ignore overflow
# and underflow

#       x = 2
#       y = 2

# 9.  Write a program which takes an integer and return the integer corresponding to the digits of the
# input written in reverse order.  For example, the reverse of 42 is 24, and the reverse of -314 is -413.

# 10.  Write a program that takea an integer and determines if that integer representation as a decimal string
# is a palindrome.  For example 121 is is a palindrome; 7 is a palindrome; -1 is not

#       x = 1221

# ------------------------------------------------------------------------------------------------------------------
# 1. Your input is an array of integers, and you have to reorder its entries so that even entries appear first.
# This is easy if you use O(n) space, where n is the length of the array.  However, you are required to solve it
# without allocating additional storage

#       A = [1, 2, 3, 4, 5]

# 2.  Write a program that takes an array A and an index i into A, and rearranges the elements
# such that all elements less than A[i] (the 'pivot') appear first, followed by elements equal to
# the pivot, followed by elements greater than the pivot
#       - Method I
#       - Method II
#       - Method III

#       A = [0, 1, 2, 0, 1, 2, 0] # [0, 0, 0, 1, 2, 1, 2]
#       pivot_index = 3

# 3.  Write a program which takes as input an array of digits encoding a nonnegative decimal integer D
#  and updates the array to represent the integer D + 1. For example, if the input is <1, 2, 9> then you
#  should update the array to <1, 3, 0>. Your algorithm should work even if it is implemented in a language
#  that has finite-prescision arthemetic.

#       A =[1, 2, 9] #[1, 3, 0]

# 4.  Write a program that takes two arrays representing integers, and return an integer representing their
# proiduct.  For example since 193707721.x -761838257287 = -147573952589676412927, if the input are
# <1,9,3,7,0,7,7,2, 1> and <-7,6,1,8,3,8,2,5,7,2,8,7>, your  function should return
# <1, 4,7, 5,7,3, 9, 5, 2, 5,8,9, 6,7, 6, 4, 1., 2,9,2,7>.

#       num1 = [1,9,3,7,0,7,7,2, 1]
#       num2 = [-7,6,1,8,3,8,2,5,7,2,8,7]
#       result = [-1, 4,7, 5,7,3, 9, 5, 2, 5,8,9, 6,7, 6, 4, 1., 2,9,2,7]

# 5.  Write a program which takes an array of n integers, where A[i] denotes the maximum you can advancxe from index i
# , and returns whether it is possible to advance to the last index starting from the beginning of the array. For example,
#  let A = (3,3,1,0,2,0,1) represent the board game, i.e., the lth entry in A is the maximum we can advance from L Then the
#  game can be won by the following sequence of advances through A: take 1 step from A[0] to A[1], then 3 steps from A[1]
# to A[4], then 2 steps from A[4]toA[6], which is the last Position. Note that A[0] =3 >= 1, 4[1] = 3 >= 3,andA[4] = 2 >= 2,
#  so all moves are valid. If A instead was (3, 2, 0, 0, 2, 0, 1), it would not possible to advance past position 3, so the
#  game cannot be won.

#       A = (2, 4, 1, 1, 0, 2, 3) # index 6


# 6.  Write a program which takes as input a sorted array and updates it so that all duplicates have been removed and the
#  remaining elements have been shifted left to fill the emptied indices.  Return the number of valid elements.  Many
# languages have library functions for performing this operation -- you cannot use these functions

#       A = [2, 3, 5, 5, 7, 11, 11, 13] #6 elements

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

# 11. Write a program that takes an integer argument and returns all the primes between 1
# and that interger. For example, if the input is 18, you should return <2, 3, 5, 7, 11, 13, 17>

#       n = 10

# 12. Given an array A of n elements and a permutation P, apply P to A

#       perm = [2, 0, 1, 3]
#       A = ['a', 'b', 'c', 'd']  # ['c', 'a', 'b', 'd']

# 13. Write a program that takes as input a permutation, and returns the next permutation
# under dictionary ordering.  If the permutation is the last permutation, return the
# empty array.  For example, if the input is <1, 0, 3, 2> your function should return
# <1, 2, 0, 3>.  If the input is <3, 2, 1, 0>, return <>.

#       perm = [1, 0, 3, 2] # <1, 2, 0, 3>.

# 15. Implement an algorithm that takes as input an array of distinct elements and
# a size, and returns a subset of the given size of the array elements. All
# subsets should be equally likely. Return the results in input array itself

#      A = [3, 7, 5, 11]
#      k = 3

# 16. Design a program that takes as input a size k, and reads packets, continuously
# maintaining a uniform random subset of size k of the read packets

#      k = 2
#      it = ['p', 'q', 'r', 't', 'u', 'v']
