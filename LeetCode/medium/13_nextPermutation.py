def nextPermutation(perm):
    """
    Do not return anything, modify nums in-place instead.
    """

    inversion_point = len(perm) - 2

    while (inversion_point >= 0 and perm[inversion_point] >= perm[inversion_point + 1]):
        inversion_point -= 1

    if inversion_point == -1:
        return []  # perm is the last permutation

    for i in reversed(range(inversion_point + 1, len(perm))):
        if perm[i] > perm[inversion_point]:
            perm[inversion_point], perm[i] = perm[i], perm[inversion_point]
            break

    perm[inversion_point + 1:] = reversed(perm[inversion_point + 1:])
    return perm


perm = [1, 2, 3]  # 1, 3, 2
print(nextPermutation(perm))
