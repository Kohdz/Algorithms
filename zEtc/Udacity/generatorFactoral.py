def prod(a, b):
    return a * b


def fact_gen():
    i = 1
    n = i
    while True:
        output = prod(n, i)
        yield output
        i += 1
        n = output


# test block
my_gen = fact_gen()
num = 5
for i in range(num):
    print(next(my_gen))


# General Factoral
def factoral(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i

    return fact


print(factoral(num))
