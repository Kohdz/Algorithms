# increment an arbitary-precsion integer

# → write a program which takes as input an array of digits encoding a nonnegative
# decimal integer D and updates the array to represent the integer D + 1.
# → For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0]
# → your algorithm should work even if it is implemented in a language that has finite-	precision arithmetic


# time O(n); n = len(A)
def plus_one(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1

    if A[0] == 10:
        # there is a carry-out so we need one more digit to restore result
        # a slick way to do this is to append a 0 at the end of the array
        # and update the first entriy to 1
        A[0] = 1
        A.append(0)
    return A


A = [1, 2, 9]
# output should be [1, 3, 0]
print(plus_one(A))
