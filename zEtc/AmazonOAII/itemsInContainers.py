def numberOfItems(s, startIndices, endIndices):
    n = len(s)
    # the left closest compartment index
    leftCompartments = [-1] * n
    # the right cloest compartment index
    rightCompartments = [-1] * n

    count = 0
    # the number items on the left side that are contained by compartments
    itemsInCompartment = {}

    for left in range(len(s)):
        if s[left] == "|":
            leftCompartments[left] = left
            itemsInCompartment[left] = count
        else:
            count += 1

            if left - 1 >= 0:
                leftCompartments[left] = leftCompartments[left - 1]
            else:
                leftCompartments[left] = -1

        right = len(s) - 1 - left
        if s[right] == "|":
            rightCompartments[right] = right
        else:
            if right + 1 < n:
                rightCompartments[right] = rightCompartments[right + 1]
            else:
                rightCompartments[right] = -1

    items = []
    for i in range(len(startIndices)):
        # convert it to 0-based index
        s, e = startIndices[i] - 1, endIndices[i] - 1
        if s > e:
            items.append(0)
        else:

            left, right = rightCompartments[s], leftCompartments[e]
            items.append(itemsInCompartment[right] - itemsInCompartment[left])

    return items


def numberOfItemsII(s, startIndices, endIndices):

    output = [0] * len(startIndices)
    skip = set()
    count = 0

    for i in range(len(startIndices)):
        if '|' not in s[startIndices[i]-1: endIndices[i]]:
            skip.add(startIndices[i])

    for i in range(len(startIndices)):
        count = 0

        if startIndices[i] in skip:
            continue
        substring = s[startIndices[i] - 1: endIndices[i]]

        initialStartPoint = substring.index('|')
        endPoint = substring.rindex('|')

        for j in range(initialStartPoint, endPoint):
            if substring[j] == '*':
                count += 1

        output[i] = count

    # for i in range(len(output)):
    #     if output[i] == -1:
    #         output[i] = 0
    return output


print(numberOfItems("|**|*|*", [1, 1], [5, 6]))     # [2,3]
print(numberOfItems("*|*|", [1], [3]))              # [0]
print(numberOfItems("*|*|*|", [1], [6]))            # [2]
print(numberOfItems("*|**|***|", [1, 2, 4, 1], [4, 6, 6, 9]))  # [0, 2, 0, 5]
print(numberOfItems("***|", [1], [1]))
