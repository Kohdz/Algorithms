
def Factoral(n):
    # input: n(natural number)
    # output: n! (the factoral of n)
    if n == 0:
        return 1
    else:
        return n*Factoral(n-1)
