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
            leftCompartments[left] = leftCompartments[
                left - 1] if left - 1 >= 0 else -1

        right = len(s) - 1 - left
        if s[right] == "|":
            rightCompartments[right] = right
        else:
            rightCompartments[right] = rightCompartments[
                right + 1] if right + 1 < n else -1

    items = []
    for i in range(len(startIndices)):
        # convert it to 0-based index
        s, e = startIndices[i] - 1, endIndices[i] - 1
        if s > e:
            items.append(0)
            continue

        left, right = rightCompartments[s], leftCompartments[e]
        items.append(itemsInCompartment[right] - itemsInCompartment[left])

    return items

print(numberOfItems("|**|*|*", [1, 1], [5, 6]))     # [2,3]
print(numberOfItems("*|*|", [1], [3]))              # [0]
print(numberOfItems("*|*|*|", [1], [6]))            # [2]
print(numberOfItems("*|**|***|", [1,2,4,1], [4,6,6,9])) # [0, 2, 0, 5]