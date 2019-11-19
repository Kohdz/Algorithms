
# time O (n) | space O (1)


def even_odd(A):
    next_even, next_odd = 0, len(A) - 1

    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1

    print(A)


A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_odd(A)
