# 6.  Write a program which takes as input a sorted array and updates it so that all duplicates have been removed and the
#  remaining elements have been shifted left to fill the emptied indices.  Return the number of valid elements.  Many
# languages have library functions for performing this operation -- you cannot use these functions


# time O(n) | space O(1)
def delete_duplicates(A):

    if not A:
        return 0

    write_index = 1
    for i in range(1, len(A)):
        if A[write_index - 1] != A[i]:
            A[write_index] = A[i]
            write_index += 1

    # Returns the number of valid entries after deletion
    return write_index


A = [2, 3, 5, 5, 7, 11, 11, 13]  # 6 elements
print(delete_duplicates(A))
