from collections import defaultdict


def getNearestCities(numOfCities, cities, xCoordinates, yCoordinates, numofQueries, queries):
    cityMap = {}  # city: (x,y)
    xMap = defaultdict(list)  # xcoord:[cities]
    yMap = defaultdict(list)  # ycoord:[cities]
    for i in range(len(cities)):
        city, x, y = cities[i], xCoordinates[i], yCoordinates[i]
        cityMap[city] = (x, y)
        xMap[x].append(city)
        yMap[y].append(city)
    res = []

    def getClosestCitiesAlongAxis(minDist, closestCities, checkXCoord, queryCity):
        queryx, queryy = cityMap[queryCity]
        cityList = xMap[queryx] if checkXCoord else yMap[queryy]
        for city in cityList:
            cityx, cityy = cityMap[city]
            if city == queryCity:
                continue
            dist = abs(cityx - queryx) if checkXCoord else abs(cityy-queryy)
            if dist < minDist:
                minDist = dist
                closestCities = [city]
            elif dist == minDist:
                closestCities.append(city)
        return minDist, closestCities

    for q in queries:
        minDist, closestCities = getClosestCitiesAlongAxis(
            float('inf'), [], True, q)
        minDist, closestCities = getClosestCitiesAlongAxis(
            minDist, closestCities, False, q)
        res.append(None) if len(
            closestCities) == 0 else res.append(min(closestCities))
    return res
# print(getNearestCities( ["c1", "c2", "c3"], [3,2,1],[3,2,3],["c1", "c2", "c3"]))




def process(queries):
    
    nearNeighbors = []
    for query in queries:
            
        # finding city info
        city_index = cities.index(query)
        x_city = x_c[city_index]
        y_city = y_c[city_index]

        # finding neighbors and minDist neighbor
        minimum_distance = float('inf')
        nearest_city = None
        for i in range(len(cities)):
            if cities[i] != query:
                if x_c[i] == x_city or y_c[i] == y_city:
                    dist = abs(x_c[i]-x_city) + abs(y_c[i] - y_city)
                    if dist < minimum_distance:
                        minimum_distance = dist
                        nearest_city = cities[i]
                    elif dist == minimum_distance:
                        if cities[i] < nearest_city:
                            nearest_city = cities[i]
        nearNeighbors.append(nearest_city)
    return nearNeighbors


numOfCities = 3
cities = ['c1', 'c2', 'c3', 'c4', 'c5']
xCoord = [3, 2, 1, 1, 1]
yCoord = [3, 2, 3, 1, 2]
numofQueries = 3
queries = ['c1', 'c2', 'c3', 'c4']
print(getNearestCities(numOfCities, cities, xCoord, yCoord, numofQueries, queries))


x_c = [3, 3, 1, 1, 1, 2]
y_c = [3, 1, 3, 1, 2, 4]
cities = ["c1", "c2", "c3", 'c4', 'c5', 'c6']
print(process(["c1", "c2", "c3", 'c4', 'c5', 'c6']))
