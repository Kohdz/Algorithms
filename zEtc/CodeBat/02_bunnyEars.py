
# We have a number of bunnies and each bunny has two big floppy ears.
#  We want to compute the total number of ears across all the bunnies recursively (without loops or multiplication).


# bunnyEars(0) → 0
# bunnyEars(1) → 2
# bunnyEars(2) → 4


# public int factorial(int n) {
#   // Base case: if n is 1, we can return the answer directly
#   if (n == 1) return 1;

#   // Recursion: otherwise make a recursive call with n-1
#   // (towards the base case), i.e. call factorial(n-1).
#   // Assume the recursive call works correctly, and fix up
#   // what it returns to make our result.
#   return n * factorial(n-1);


def bunnyEars(n):

    if n == 0:
        return 0

    return 2 + bunnyEars(n-1)


n = 0
n2 = 1
n3 = 2
print(bunnyEars(n))
print(bunnyEars(n2))
print(bunnyEars(n3))
