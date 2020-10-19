import heapq

def maxUnits(num, boxes, unitSize, unitsPerBox, truckSize):
    heap = []

    for i in range(len(boxes)):
        units_per_box = unitsPerBox[i]
        heapq.heappush(heap, (-units_per_box, boxes[i]))

    ret = 0

    while truckSize > 0 and heap:
        curr_max = heapq.heappop(heap)
        max_boxes = min(truckSize, curr_max[1])
        truckSize -= max_boxes
        ret += max_boxes * (curr_max[0] * -1)
    
    return ret


# test cases
print(maxUnits(3, [1,2,3], 3, [3,2,1], 3))
print(maxUnits(3, [2,5,3], 3, [3,2,1], 50))