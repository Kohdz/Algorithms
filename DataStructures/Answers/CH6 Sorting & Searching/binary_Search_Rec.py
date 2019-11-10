def binarySearchRec(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) //2 
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binarySearchRec(alist[:midpoint], item)
            else:
                return binarySearchRec(alist[midpoint +1], item)


testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(binarySearchRec(testlist, 3))
print(binarySearchRec(testlist, 13))