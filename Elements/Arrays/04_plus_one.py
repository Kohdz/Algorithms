# increment an arbitary-precsion integer


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
