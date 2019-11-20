y = [1, 2]
x = []

if y:
    print(1)

if x:
    print(2)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x**2 for x in a if x % 2 == 0]
print(squares)
