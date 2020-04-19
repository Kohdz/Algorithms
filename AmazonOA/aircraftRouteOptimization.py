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
