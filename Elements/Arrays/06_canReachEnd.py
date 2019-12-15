# write a program which takes an array on n integers, where A[i] denotes the max you can advance from index i,
# and returns whether it is possible to advance to the last index starting from the beggining of the array


def can_reach_end(A):
    furthest_reach_so_far, last_index = 0, len(A) - 1

    i = 0

    while i <= furthest_reach_so_far and furthest_reach_so_far < last_index:
        furthest_reach_so_far = max(furthest_reach_so_far, A[i] + i)
        i += 1

    return furthest_reach_so_far >= last_index


A = [2, 4, 1, 1, 0, 2, 3]
print(can_reach_end(A))
