def distanceBetween(a, b):
    return abs(a - b)

def getIdxAtMinValue(array):

    getIdxAtMinValue = 0
    minValue = float('inf')

    for i in range(len(array)):
        currentValue = array[i]
        if currentValue < minValue:
            minValue = currentValue
            idxAtMinValue = i
    
    return idxAtMinValue

# O(b^ * r) time | O(b) space
def apartmentHunting(blocks, reqs):
    maxDistancesAtBlocks = [float('-inf') for block in blocks]
    
    for i in range(len(blocks)):
        for req in reqs:
            closestReqDistance = float('inf')
            for j in range(len(blocks)):
                if blocks[j][req]:
                    closestReqDistance = min(closestReqDistance, distanceBetween(i, j))
            maxDistancesAtBlocks[i] = max(maxDistancesAtBlocks[i], closestReqDistance)

    return getIdxAtMinValue(maxDistancesAtBlocks)


def getMinDistances(blocks, req):
    minDistances = [0 for block in blocks]
    closestReqIdx = float("inf")

    # pgym, gym, store, school]
    for i in range(len(blocks)):

        # if requirment is on block, closest is at i 
        if blocks[i][req]:
            closestReqIdx = i
        minDistances[i] = distanceBetween(i, closestReqIdx)
    for i in reversed(range(len(blocks))):
        if blocks[i][req]:
            closestReqIdx = i
        minDistances[i] = min(minDistances[i], distanceBetween(i, closestReqIdx))
    return minDistances


#     
def getMaxDistancesAtBlocks(blocks, minDistancesFromBlocks):
    '''
    gym: [0, 0, 1, 1, 0]
    store: [2, 3, 1, 1, 0]
    school: [0, 4, 1, 1, 0]
    '''

    maxDistancesAtBlocks = [0 for blocks in blocks]
    for i in range(len(blocks)):
        # idx 0 -> 0 2 0 -> 2
        # idx 1 -> 0, 3, 4 -> 7
        # we are mapping gym, store, school and getting min distances 
        minDistancesFromBlock = list(map(lambda distances: distances[i], minDistancesFromBlocks))
        
        # this is 4 if our idx = 1
        maxDistancesAtBlocks[i] = max(maxDistancesAtBlocks)

    return maxDistancesAtBlocks

# Time O(b * r) | Space O(b * r)
def apartmentHuntingOptimal(blocks, reqs):

    # the min distances from all of the blocks is a map of the requirements
    # where for each requirement we get all of the min distances of that requirement
    # from every single block
    minDistancesFromBlocks = list(map( lambda req: getMinDistances(blocks, req), reqs)) # O(br)
    maxDistancesAtBlocks = getMaxDistancesAtBlocks(blocks, minDistancesFromBlocks) # O(br)
    getIdxAtMinValue(maxDistancesAtBlocks) # O(b)