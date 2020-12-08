# Prime Air Route

# Each aircraft should be assigned two shipping routes at once: one forward route and one return route. Due to the complex scheduling
# of flight plans,all aircraft have a fixed maximum operating travel distance, and cannot be scheduled to fly a shipping route that requires
# more travel distance than the prescribed maximum operating travel distance.
# The goal of the system is to optimize the total operating travel distance of a given aircraft.
# A forward/return shipping route pair is considered to be “optimal” if there does not exist another pair that has a higher operating travel
#  distance than this pair, and also has a total less than or equal to the maximum operating travel distance of the aircraft.

# For example, if the aircraft has a maximum operating travel distance of 3000 miles,
# a forward/return shipping route pair using a total of 2900 miles would be optimal if there does not exist a pair that uses a total operating
# travel distance of 3000 miles,
# but would not be considered optimal if such a pair did exist.Your task is to write an algorithm to optimize the sets of forward/return shipping
#  route pairs that allow the aircraft to be optimally utilized, given a list of forward shipping routes and a list of return shipping routes.

# Examples 1:
# maxTravelDist=7000
# forwardRouteList=[[1,2000][2,4000][3,6000]]
# returnRouteList=[[1,2000]]
# Output: [[2,1]]

# Examples 1:
# maxTravelDist=10000
# forwardRouteList=[[1,3000][2,5000][3,7000],[4,10000]
# returnRouteList=[[1,2000][2,3000][3,4000][4,5000]]
# Output: [[2,4],[3,2]]


# Two pointers tragety
# sorting takes logn time
# space = O()
def optimalFlightPath(maxTDist, fList, rList):
    fList.sort(key=lambda x : x[1])
    rList.sort(key=lambda x : x[1])
    
    maxHere = 0
    result = []
    
    f, r = 0, len(rList)-1
    
    while f<len(fList) and r >= 0:
        maxH = fList[f][1] + rList[r][1]
        if maxH <= maxTDist:
            if maxH > maxHere:
                maxHere = maxH
                result = [[fList[f][0],rList[r][0]]]
            elif maxH == maxHere:
                result.append([fList[f][0],rList[r][0]])
            f += 1
        else:
            r -= 1
    return result


print(optimalFlightPath(11, [[1, 5], [2, 5]], [ [1, 5], [2, 5] ]))
print(optimalFlightPath(10, [[1, 5], [2, 5]], [ [1, 5], [2, 5] ]))
print(optimalFlightPath(20, [[1, 8], [2, 7], [3, 14]], [[1, 5], [2, 10], [3, 14]]))
print(optimalFlightPath(20, [[1, 8], [2, 15], [3, 9]], [[1, 8], [2, 11], [3, 12]]))
print(optimalFlightPath(7000, [[1, 2000], [2, 4000], [3, 6000]], [[1, 2000]]))
print(optimalFlightPath(10000, [[1, 3000], [2, 5000], [3, 7000], [4, 10000]], [[1, 2000], [2,3000], [3,4000], [4,5000]]))