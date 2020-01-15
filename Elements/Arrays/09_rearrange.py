# writr a program that takes an A of n numbers, and rearranges A's
# elements to get a new array B having the property that 
# B[0] <= B[1] >= B[2] <= B[3] >= B[4] <= B[5] >= ...

def rearrange(A):

    for i in range(len(A)):
        A[i: i + 2] = sorted(A[i:i + 2], reverse= i % 2)

    return A

A = [2, 1, 4, 6, 3, 6, 4, 2]
print(rearrange(A))