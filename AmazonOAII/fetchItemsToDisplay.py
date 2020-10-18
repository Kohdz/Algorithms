

def fetchItemsToDisplay(numOfItems, items, sortParameter, sortOrder, itemsPerPage, pageNumber):
    order = False
    if sortOrder == 1:
        order = True
    
    res = []
    currPage = 0
    currItems = 1
    sortKey = [lambda x: x, lambda x: items[x][0], lambda x: items[x][1]]
    for name in sorted(items, reverse=order, key=sortKey[sortParameter]): # sort: O(nlogn) loop: O(n) -> Total: O(nlogn + n) = O(nlogn)
        # print(name, items[name]) # Uncomment to see the sorting order
        if currPage > pageNumber:
            break
        if currPage == pageNumber:
            res.append(name)
        if currItems == itemsPerPage:
            currItems = 1
            currPage += 1
        currItems += 1
    
    return res

# Time: O(nlogn)
# Space: O(n) 

items = {'item1': (10,15), 'item2': (3,4), 'item3': (17,8)}
print(fetchItemsToDisplay(3, items, 1, 0, 2, 1)) # Output: ["item3"]
print(fetchItemsToDisplay(3, items, 0, 0, 2, 1)) # Output: ["item3"]
print(fetchItemsToDisplay(3, items, 2, 0, 2, 1)) # Output: ["item1"]
print(fetchItemsToDisplay(3, items, 2, 0, 2, 2)) # Output: []
print(fetchItemsToDisplay(3, items, 1, 0, 2, 0)) # Output: ["item2", "item1"]
print(fetchItemsToDisplay(3, items, 1, 1, 5, 0)) # Output: ["item3", "item1", "item2"]
