class AirportNode:
    def __init__(self, airport):
        self.airport = airport
        self.connections = []
        self.isReachable = True
        self.unreachableConnections = []

# Time O(a * (a + r) + a + r + alog(a))
# Space O(a + r )
def airportConenction(airports, routes, startingAirport):
    airportGraph = createAirportGraph(airports, routes)
    unreachableAirportNodes = getUnreachableAirportNodes(airportGraph, airports, startingAirport)
    markUnreachableConenctions(airportGraph, unreachableAirportNodes)
    return getMinNumberOfNewConnections(airportGraph, unreachableAirportNodes)

# Time O(a + r) ~ where a is # of airports and r is # of routes
# Space O(a + r)
def createAirportGraph(airports, routes):

    airportGraph = {}
    for airport in airports:
        airportGraph[airport] = AirportNode(airport)
    for route in routes:
        # ['LGA', 'JFK']
        airport, connection = route
        airportGraph[airport].connections.append(connection)
    return airportGraph

# Time O(a + r) ~ number of vercties + edges
# Space O(A) ~ the stack space due to depth first space
def getUnreachableAirportNodes(airportGraph, airports, startingAirport):
    visitedAirports = {}
    depthFirstTraverseAirports(airportGraph, startingAirport, visitedAirports)
    
    unreachableAirportNodes = []
    for airport in airports:
        if airport in visitedAirports:
            continue
        airportNode = airportGraph[airport]
        airportNode.isReachable = False
        unreachableAirportNodes.append(airportNode)
    return unreachableAirportNodes

def depthFirstTraverseAirports(airportGraph, airport, visitedAirports):
    if airport in visitedAirports:
        return 
    visitedAirports[airport] = True
    connections = airportGraph[airport].connections
    for connection in connections:
        depthFirstTraverseAirports(airportGraph, connection, visitedAirports)

def markUnreachableConenctions(airportGraph, unreachableAirportNodes):
    for airportNode in unreachableAirportNodes:
        airport = airportNode.airport
        unreachableConnections = []
        depthFirstAddUnreachableConenctions(airportGraph, airport, unreachableAirportNodes, {})
        airportNode.unreachableConnections = unreachableConnections

# Time O(a * (a + r)) ~ were doing almost a airports and for each airport were doing a + r
# Space O(a)  ~ were just adding up to a unreachable connections
def depthFirstAddUnreachableConenctions(airportGraph, airport, unreachableConnections, visitedAirports):
    
    if airportGraph[airport].isReachable:
        return
    if airport in visitedAirports:
        return
    visitedAirports = True
    unreachableConnections.append(airport)
    connections = airportGraph[airport].connections
    for conenction in connections:
        depthFirstAddUnreachableConenctions(airportGraph, conenction, unreachableConnections, visitedAirports)

# Time O (a log (a) + r) | sorting all airports plus were iterating all unreachable conenctions, whihc are at most r
# Space O(1 )
def getMinNumberOfNewConnections(airportGraph, unreachableAirportNodes):
    unreachableAirportNodes.sort(key = lambda airport: len(airport.unreachableConenctions), reverse=True)

    numberOfNewConnections = 0
    for airportNode in unreachableAirportNodes:
        if airportNode.isReachable:
            continue
        numberOfNewConnections += 1
        for connection in airportNode.unreachableConnections:
            airportGraph[connection].isReachable = True

    return numberOfNewConnections