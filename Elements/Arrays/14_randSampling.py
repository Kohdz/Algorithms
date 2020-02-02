# Implement an algorithm that takes as input an array of distinct elements and
# a size, and returns a subset of the given size of the array elements. All
# subsets should be equally likely. Return the results in input array itself

import random


def random_sampling(k, A):
    for i in range(k):
        # Generate a random index in [i, len(A) - 1].
        r = random.randint(i, len(A) - 1)
        A[i], A[r] = A[r], A[i]

A = [3, 7, 5, 11]
k = 3

print(random_sampling(k, A))