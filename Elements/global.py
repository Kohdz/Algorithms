# 1. Write A Program to count the number of bits set to 1

    # x = 12 # 1100

# 2. How would you compute the parity of a very large number of 64-bit words
    # - Method 1
    # - Method 2
    # - Method 3

    # x = 12 # 1100

# 3. Swap Bits. Swap the 1-index bit


    # x = 0b01001001 #00001011

# 4. Write a program that takes a 64-th bit unsigned integer and returns the 64-bit unsigned
# integer consisting of the bits of the input in reverse order.  For example, the input is
# (1110000000000001), the output should be (1000000000000111).

    # x = 0b1110000000000001 #1000000000000111

# 5. Define the weight of a nonnegative integer x to be the number of bits that are set to 1
# in its binary representation.  For example, since 92 in base-2 equals (1011100), the weight
# of 92 is 4.  Write a program which takes as input a nonnegative integer x and returns a 
# number y which is not equal to x, but has the same weight as x and their difference, |y - x|,
# is as small as possible.  You can assume x is not 0, or all 1s.  For example, if x = 6,
# you should return 5.  You can assume the integer fits in 64 bits.

    # x = 6 #5

#  5. Write a program that multiplies two nonnegative integers.  The only operators you are
#  allowed to use are
#     - assignment
#     - the bitwise operators >>, <<, |, &, ~, ^, and
#     - equality checks and Boolean combinations thereof

# ------------------------------------------------------------------------------------------------------------------

# 1.  Write a program that takes an array A and an index i into A, and rearranges the elements such that all elements less than A[i]
# (the 'pivot') appear first, followed by elements equal to the pivot, followed by elements greater than the pivot
    # - Method I
    # - Method II
    # - Method III
    
    # A = [0, 1, 2, 0, 1, 2, 0] # [0, 0, 0, 1, 2, 1, 2]
    # pivot_index = 3 

# 2.  Write a program which takes as input an array of digits encoding a nonnegative decimal integer D and updates the array to represent
# the integer D + 1. For example, if the input is <1, 2, 9> then you should update the array to <1, 3, 0>. Your algorithm should work even if
# it is implemented in a language that has finite-prescision arthemetic.

    # A =[1, 2, 9] #[1, 3, 0]

# 3.  Write a program that takes two arrays representing integers, and return an integer representing their proiduct.  For example since
#  193707721.x -761838257287 = -147573952589676412927, if the input are  <1,9,3,7,0,7,7,2, 1> and <-7,6,L,8,3,8,2,5,7,2,8,7>, your 
#  function should refum <-1, 4,7, 5,7,3, 9, 5, 2, 5,8,9, 6,7, 6, 4, 1., 2,9,2,7>.


    # num1 = [1,9,3,7,0,7,7,2, 1]
    # num2 = [-7,6,L,8,3,8,2,5,7,2,8,7]
    # result = [-1, 4,7, 5,7,3, 9, 5, 2, 5,8,9, 6,7, 6, 4, 1., 2,9,2,7]

# 4.  Write a program which takes an array of n integers, where A[i] denotes the maximum you can advancxe from index i, and returns whether
# it is possible to advance to the last index starting from the beginning of the array.   For example, let A = (3,3,1,0,2,0,1) represent the 
# board game, i.e., the lth entry in A is the maximum we can advance from L Then the game can be won by the following sequence of
# advances through A: take 1 step from A[0] to A[1], then 3 steps from A[1] to A[4], then 2 steps from A[4]toA[6], which is the last Position.
# Note that A[0] =3 >= 1, 4[1] = 3 >= 3,andA[4] = 2 >= 2, so all moves are valid. If A instead was (3, 2, 0, 0, 2, 0, 1), it would not possible
# to advance past position 3, so the game cannot be won.

    # A = (2, 4, 1, 1, 0, 2, 3) # index 6


# 5.  Write a program which takes as input a sorted array and updates it so that all duplicates have been removed and the remaining elements
# have been shifted left to fill the empited indices.  Return the number of valid elements.  Many languages have libary functions for performing
# this operation -- you cannot use thse functions

    A = [2, 3, 5, 5, 7, 11, 11, 13] #6 elements