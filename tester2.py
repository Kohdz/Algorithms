

# even to fron of list

ordList = [1, 2, 3, 4, 5, 6, 7, 8]


def even_odd(ordList):
    even, odd = 0, len(ordList)-1

    while even < odd:
        if ordList[even] % 2 == 0:
            even += 1
        else:
            ordList[even], ordList[odd] = ordList[odd], ordList[even]
            odd -= 1

    return ordList


print(even_odd(ordList))
