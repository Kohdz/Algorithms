

def plus_one(A):

    # add 1 to last element
    # loop through element end to front
    # add one and change number to 0
    # brake if not 10

    # check if 1th element is 10
    # and adujust

    A[-1] += 1

    for i in reversed(range(1, len(A))):

        if A[i] != 10:
            break

        A[i] = 0
        A[i-1] += 1

    if A[0] == 10:
        A[0] = 1
        A.append(0)

    return A


A = [9, 9]
print(plus_one(A))
