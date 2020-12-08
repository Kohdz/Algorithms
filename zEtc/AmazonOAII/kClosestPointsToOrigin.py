from heapq import heappush, heappop

def kClosest(points, K):

    heap = []
    
    for i in range(K):
        heappush(heap, (-getDist(points[i]), points[i]))
        
    for i in range(K, len(points)):
        
        dist = getDist(points[i])
        
        if dist < -heap[0][0]:
            heappop(heap)
            heappush(heap, (-dist, points[i]))
            
    return [heappop(heap)[1] for _ in range(K)]
    
def getDist(point):
    dist = (point[0]**2 + point[1]**2) ** .05
    
    return dist
