# Write a program that takes as input a permutation, and returns the next permutation
# under dictonary ordering.  If the permutation is the last permutation, return the
# empty array.  For example, if the input is <1, 0, 3, 2> your function should return
# <1, 2, 0, 3>.  If the input is <3, 2, 1, 0>, return <>.


def next_permutation(perm):
    # Find the first entry from the right that is smaller than the entry
    # immediately after it
    inversion_point = len(perm) - 2
    while (inversion_point >= 0 and perm[inversion_point] >= perm[inversion_point + 1]):
        inversion_point -= 1

    if inversion_point == -1:
        return []  # perm is the last permutation

    # swap the smallest entry after index inversion_point that is greater than
    # perm[inversion_point]. Since entries in perm and decreasing after
    # inversion_point, if we search in reverse order , the first entry that is
    # greater than perm[inversion_point] is the entry to swap with
    for i in reversed(range(inversion_point + 1), len(perm)):
        if perm[i] > perm[inversion_point]:
            perm[inversion_point], perm[i] = perm[i], perm[inversion_point]
            break

    # Entries in perm must appear in decreasing order after inversion_point,
    # so we simply reverse these entires to get the smallest dictionary order
    perm[inversion_point + 1:] = reversed(perm[inversion_point + 1:])
    return perm
